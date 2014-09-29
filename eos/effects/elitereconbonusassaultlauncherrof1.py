# eliteReconBonusAssaultLauncherROF1
#
# Used by:
# Ship: Huginn
# Ship: Lachesis
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Recon Ships").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Missile Launcher Rapid Light",
                                  "speed", ship.getModifiedItemAttr("eliteBonusReconShip1") * level)
