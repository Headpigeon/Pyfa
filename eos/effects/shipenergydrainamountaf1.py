# shipEnergyDrainAmountAF1
#
# Used by:
# Ship: Cruor
# Ship: Sentinel
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Frigate").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Vampire",
                                  "powerTransferAmount", ship.getModifiedItemAttr("shipBonusAF") * level)
