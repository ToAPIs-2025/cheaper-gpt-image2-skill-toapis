import importlib.util,sys,unittest,tempfile,json,base64,io,os
from pathlib import Path
from unittest.mock import patch
import argparse
p=argparse.ArgumentParser();p.add_argument('--upstream',type=Path,required=True);a,extra=p.parse_known_args();sys.path.insert(0,str(a.upstream.resolve()/'src'));sys.argv=[sys.argv[0]]+extra
from gpt_image_cli.toapis import ToAPIsClient,build_request,normalize_origin
from gpt_image_cli import cli
class AdapterTests(unittest.TestCase):
    def kwargs(self):return {'model':'gpt-image-2-vip','prompt':'fixture','size':'1024x1024','quality':'low','n':1,'moderation':'low'}
    def test_parameter_mapping_and_standard_omits_quality(self):
        body,_=build_request(self.kwargs());self.assertEqual(body,{'model':'gpt-image-2-vip','prompt':'fixture','size':'1:1','quality':'low','resolution':'1K','n':1})
        body,_=build_request({**self.kwargs(),'model':'gpt-image-2'});self.assertNotIn('quality',body);self.assertNotIn('moderation',body)
    def test_unsupported_flags_fail_before_network(self):
        for args in [{'n':2},{'mask':'mask.png'},{'background':'transparent'},{'output_format':'jpeg'},{'input_fidelity':'high'},{'model':'gpt-image-2.5-flare'}]:
            with self.subTest(args=args),self.assertRaises(ValueError):build_request({**self.kwargs(),**args})
    def test_origin_normalization_and_blocked_hosts(self):
        self.assertEqual(normalize_origin('https://toapis.cn/v1/'),'https://toapis.cn')
        for base in ['http://toapis.cn','https://toapis.cn:8443','https://evil.example/v1','https://user:pass@toapis.cn','https://toapis.cn/v1/v1']:
            with self.assertRaises(ValueError):normalize_origin(base)
    def client(self,d):
        client=ToAPIsClient('fixture-key',state_dir=d);client._asset=lambda url:b'fixture-png';return client
    def test_completed_task_reuse_no_second_post_and_real_writer(self):
        with tempfile.TemporaryDirectory() as d:
            c=self.client(d);calls=[]
            def query(path,body=None,content_type=None):
                calls.append((path,body));return {'id':'fixture-task'} if body is not None else {'status':'completed','result':{'data':[{'url':'https://assets.example/result.png'}]}}
            c._json=query;r=c.generate(**self.kwargs());c.generate(**self.kwargs());self.assertEqual(sum(b is not None for _,b in calls),1)
            saved=cli.write_outputs(r.data,Path(d)/'saved.png',1);self.assertEqual(saved[0].read_bytes(),b'fixture-png')
    def test_uncertain_post_blocks_resubmission(self):
        with tempfile.TemporaryDirectory() as d:
            c=self.client(d);calls=[]
            def fail(*args):calls.append(args);raise TimeoutError()
            c._json=fail
            with self.assertRaises(RuntimeError):c.generate(**self.kwargs())
            with self.assertRaisesRegex(RuntimeError,'Prior generation'):c.generate(**self.kwargs())
            self.assertEqual(len(calls),1)
    def test_failed_task_is_kept(self):
        with tempfile.TemporaryDirectory() as d:
            c=self.client(d);calls=[]
            def query(path,body=None,content_type=None):
                calls.append((path,body));return {'id':'failed-task'} if body is not None else {'status':'failed'}
            c._json=query
            for _ in range(2):
                with self.assertRaises(RuntimeError):c.generate(**self.kwargs())
            self.assertEqual(sum(b is not None for _,b in calls),1);self.assertEqual(c.last_receipt['task_id'],'failed-task')
    def test_original_edit_closes_file_and_upload_maps_reference(self):
        with tempfile.TemporaryDirectory() as d:
            folder=Path(d);ref=folder/'input.png';ref.write_bytes(b'png');c=self.client(folder/'state');calls=[]
            def query(path,body=None,content_type=None):
                calls.append((path,body))
                if path=='uploads/images':self.assertIn(b'filename="reference.png"',body);return {'data':{'url':'https://assets.example/ref.png'}}
                return {'id':'edit-task'} if body is not None else {'status':'completed','result':{'data':[{'url':'https://assets.example/out.png'}]}}
            c._json=query
            with patch.object(sys,'argv',['gpt-image','--provider','toapis','--model','gpt-image-2-vip','--quality','low','-p','fixture','-i',str(ref)]):args=cli.parse_args()
            cli.call_edit(c,args);self.assertEqual(calls[1][1]['reference_images'],['https://assets.example/ref.png'])
    def test_toapis_branch_runs_original_main_and_dry_run_needs_no_key(self):
        with patch.object(sys,'argv',['gpt-image','--provider','toapis','--model','gpt-image-2-vip','--quality','low','-p','fixture','--dry-run']),patch.dict(os.environ,{},clear=True),patch('urllib.request.OpenerDirector.open',side_effect=AssertionError('No network allowed')):
            self.assertEqual(cli.main(),0)
if __name__=='__main__':unittest.main()
