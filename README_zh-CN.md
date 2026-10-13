# 更便宜的 GPT Image2 Skill · ToAPIs 低价生图 CLI

[English](README.md) · [中文](README_zh-CN.md) · [Pricing](PRICING.md) · [Charges](COSTS.md) · [Original outputs](GALLERY.md)

**$0.0019/张**：ToAPIs `gpt-image-2-vip` / low / 1K，本次实扣与Key目录报价一致。基于 wuyoscar/GPT-Image2-Skill 的真实CLI，新增异步Provider；2026-10-13完成 **3张image-2(vip)生图＋1张标准对照**，涵盖产品主视觉、等距场景和参考改图。

## 演示

![Real outputs and CLI guide](screenshots/cn/01-cover.png)

![Original reference edit](screenshots/cn/03-reference.png)

实际合计 **4.14积分=$0.0207**。账号持有人确认VIP每张0.38积分、标准图3积分；按1积分=$0.005换算。API billing仍为空，来源与逐项记录分别保留。 [逐项消费](COSTS_zh-CN.md).

## 复现：先dry-run，再显式付费调用

Python 3.11+、Git。本次Python3.12、openai3.29.0、python-dotenv1.2.4。稀疏检出只取CLI和测试，避免下载完整图库。此仓库为社区补丁/教程，不代表作者官方版本或已经建立合作。

```bash
git clone https://github.com/ToAPIs-2025/cheaper-gpt-image2-skill-toapis.git
git clone --filter=blob:none --no-checkout https://github.com/wuyoscar/GPT-Image2-Skill.git gpt-image-upstream
git -C gpt-image-upstream sparse-checkout init --cone
git -C gpt-image-upstream sparse-checkout set src tests skills/gpt-image/scripts
git -C gpt-image-upstream checkout 9f8aa1a44a4a5c0f5a5d6e45eed564b3e2d5b87f
cd cheaper-gpt-image2-skill-toapis
git -C ../gpt-image-upstream apply ../cheaper-gpt-image2-skill-toapis/adapter.patch
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements-demo.txt
python -m pip install -e ../gpt-image-upstream
cp .env.example .env
# Windows PowerShell: Copy-Item .env.example .env
# Configure TOAPIS_API_KEY privately; never paste it into posts.
python run_cases.py --upstream ../gpt-image-upstream
python tests/test_adapter.py --upstream ../gpt-image-upstream
python tests/run_upstream_tests.py --upstream ../gpt-image-upstream
python run_cases.py --upstream ../gpt-image-upstream --key-file .env --live --case vip-product
```

首个live命令只生成一张。生成好的结果和private-state必须保留；提交未返回ID时先查后台日志，禁止自动重发。要跑全部四例，可执行下面的命令；已有成功evidence会跳过，已提交任务会查询原ID。

```bash
python run_cases.py --upstream ../gpt-image-upstream --key-file .env --live
```

全部四例按本次目录报价$0.0207；runner先查价，若估算超过独立$0.10子上限则停止。首例必须先于参考改图；一张输出也可直接作为下一条CLI的-i输入复用。

## 直接复用原CLI

```bash
gpt-image --provider toapis --model gpt-image-2-vip \
  --quality low --resolution 1K --size square \
  -p "A fictional cobalt-blue perfume bottle on travertine, no text or logo" \
  -f result.png --dry-run
# Remove --dry-run only when ready for a paid generation.
gpt-image --provider toapis --model gpt-image-2-vip \
  --quality low --resolution 1K --size square \
  -p "Move the reference bottle to a sunlit botanical studio, no text or logo" \
  -i result.png -f edited.png
```

第二条命令是付费改图示例，运行前先生成result.png并核对费用。安装后也可用python -m gpt_image_cli.cli或本地Skill launcher启动CLI；本次仅检查launcher --help，未在Claude/Codex/OpenClaw等Agent里跑完整流程。远程uvx拉取未打补丁的上游版本不会带此ToAPIs Provider。

## 接口差异与最小补丁

固定上游SHA： `9f8aa1a44a4a5c0f5a5d6e45eed564b3e2d5b87f`.

修改src/gpt_image_cli/cli.py，新增src/gpt_image_cli/toapis.py。保留默认OpenAI路径；--provider toapis才走新适配。原call_generate、call_edit及write_outputs真实执行，异步结果转成CLI已有的b64_json数据结构后保存原始图片字节。

| 核对项 | ToAPIs实现 |
|---|---|
| Origin/auth | https://toapis.cn or https://toapis.com; normalize optional /v1; Bearer Key |
| Model | gpt-image-2-vip + low, or gpt-image-2 without quality |
| Size | CLI 1024x1024 → size 1:1; resolution 1K; actual pixels recorded separately |
| References | POST /v1/uploads/images → reference_images:[URL] |
| Submit | POST /v1/images/generations → persist id; generation POST not retried |
| Query | GET /v1/images/generations/{id}; 8s polling, 600s limit |
| Output | result.data[0].url → credential-free download → b64_json → original writer |

当前只支持n=1、PNG、不透明图片、上述两个模型。拒绝蒙版、input_fidelity、JPEG/WebP输出、compression/user及其他模型；原默认moderation参数没有对应旋钮，适配时省略。resolution为档位，不保证固定像素；其他尺寸/档位有校验但本次仅1:1/1K实测。

## 验证范围与证据

8项适配离线测试、18项原项目离线测试通过；Windows SDK3清空环境的测试用例需预先建立系统信任证书上下文，测试harness未关闭TLS验证。4次真实CLI调用完成。首张曾在包装脚本输出编码处中断，结果与任务已保留，修复后复用原ID，无第二次生图提交；记录的短耗时只是恢复查询，不作为生成速度宣传。

[Prompts](cases/briefs.json) · [Task IDs, requests, hashes](evidence/runs.json) · [Sanitized CLI logs](evidence/vip-reference-edit-cli.txt)

## 上游归属与API入口

[wuyoscar/GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) · [Fixed source](https://github.com/wuyoscar/GPT-Image2-Skill/tree/9f8aa1a44a4a5c0f5a5d6e45eed564b3e2d5b87f) · [MIT license](LICENSE). Preserve upstream notices. All case prompts are original; no upstream gallery artwork is republished.

[查看ToAPIs图片API与价表](https://go2v.toapis.com/1013_gptskill_cheaper_gh_cn) · [X screenshot reuse](SCREENSHOT_GUIDE_zh-CN.md)
