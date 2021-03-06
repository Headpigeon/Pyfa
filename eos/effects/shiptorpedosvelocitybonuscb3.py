# shipTorpedosVelocityBonusCB3
#
# Used by:
# Variations of ship: Raven (3 of 4)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Battleship").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Torpedoes"),
                                    "maxVelocity", ship.getModifiedItemAttr("shipBonusCB3") * level)
