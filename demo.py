import os

import dg_sdk


dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(
    private_key=os.environ["private_key"],
    public_key=os.environ["public_key"],
    sys_id=os.environ["sys_id"],
    product_id=os.environ["product_id"],
    huifu_id=os.environ["huifu_id"],
)

result = dg_sdk.Member.query_user_detail(
    huifu_id=os.environ["user_huifu_id"],
)

print(result)
