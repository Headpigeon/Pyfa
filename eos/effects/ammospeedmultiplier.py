# ammoSpeedMultiplier
#
# Used by:
# Charges from group: Festival Charges (8 of 8)
# Charges from group: Survey Probe (3 of 3)
# Charge: Warp Disrupt Probe
type = "passive"
def handler(fit, module, context):
    module.multiplyItemAttr("speed", module.getModifiedChargeAttr("speedMultiplier") or 1)
