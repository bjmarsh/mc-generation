from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'T2tb_LHEtoGENSIM'
config.General.workArea = 'tasks'
config.General.transferOutputs = True
config.General.transferLogs = True


config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'LHEtoGENSIM_cfg.py'
config.JobType.inputFiles = ['merged_425.lhe']


config.Data.primaryDataset = 'SMS-T2tb_2J_mStop-425_mChgno-230_mLSP-2225_MCRUN2_74_V9-v1'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
NJOBS = 500  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.publishDataName = 'CRAB3_T2tb_GENSIM'

config.Site.storageSite = 'T2_US_UCSD'
