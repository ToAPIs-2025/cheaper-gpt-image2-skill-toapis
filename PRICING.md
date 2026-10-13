# ToAPIs rates and validated models

Read-only GET /v1/pricing with this test key on 2026-10-13. Returned account/group discounts are already included. Check applicable rates with your own key; this catalog does not lock a price. All image requests use n=1.

| Exact model | Tier | USD catalog rate | Validated here |
|---|---|---:|---|
| gpt-image-2-vip | low / 1K | $0.0019/request | 2 generations + 1 reference edit |
| gpt-image-2-vip | low / 2K, 4K | $0.00425, $0.00525/request | Quoted, not generated |
| gpt-image-2-vip | medium / 1K | $0.0169/request | Quoted, not generated |
| gpt-image-2-vip | high / 1K | $0.0675/request | Quoted, not generated |
| gpt-image-2 | n=1 / 1K | $0.015/request | 1 standard control; quality omitted |
| gpt-image-2 | n=1 / 2K, 4K | $0.020, $0.025/request | Quoted, not generated |

“Cheaper” compares VIP low/1K at $0.0019 with standard 1K at $0.015 in this run, about 87.3% lower. Different routes and quality settings; no equivalent-quality or lowest-price promise. Image 2.5, transparency, masking and video are not validated through this ToAPIs adapter. Other upstream routes do not establish support here.

[Actual charges](COSTS.md) · [Rate snapshot](evidence/pricing.json) · [Current ToAPIs prices](https://toapis.com/en/pricing) · [Billing contract](https://docs.toapis.com/docs/en/api-reference/account/pricing)
