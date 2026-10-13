# ToAPIs价表与可用模型

2026-10-13用本次Key查询GET /v1/pricing。报价含返回的账户/组折扣；用户应先查自己的适用价格，报价不锁价。所有图片请求n=1。

| 精确模型 | 档位 | USD目录报价 | 本项目验证 |
|---|---|---:|---|
| gpt-image-2-vip | low / 1K | $0.0019/次 | 2次文生图+1次参考改图 |
| gpt-image-2-vip | low / 2K、4K | $0.00425、$0.00525/次 | 有报价，未生成 |
| gpt-image-2-vip | medium / 1K | $0.0169/次 | 有报价，未生成 |
| gpt-image-2-vip | high / 1K | $0.0675/次 | 有报价，未生成 |
| gpt-image-2 | n=1 / 1K | $0.015/次 | 1次标准对照，省略quality |
| gpt-image-2 | n=1 / 2K、4K | $0.020、$0.025/次 | 有报价，未生成 |

“更便宜”指本次VIP low/1K报价$0.0019对比standard 1K $0.015，低约87.3%。不同通道与画质档位，不保证同质量或全平台最低价。2.5、透明输出、蒙版以及视频均未在本ToAPIs补丁验收；上游支持它们的其他路径不等于本适配支持。

[Actual charges](COSTS_zh-CN.md) · [Rate snapshot](evidence/pricing.json) · [Current ToAPIs prices](https://toapis.com/en/pricing) · [Billing contract](https://docs.toapis.com/docs/en/api-reference/account/pricing)
