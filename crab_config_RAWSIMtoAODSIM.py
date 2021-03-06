from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'T2tb_AODSIM'
config.General.workArea = 'tasks'
config.General.transferOutputs = True
config.General.transferLogs = True


config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'RAWSIMtoAODSIM_cfg.py'

config.Data.primaryDataset = 'SMS-T2tb_2J_mStop-425_mChgno-230_mLSP-2225_MCRUN2_74_V9-v1'
config.Data.userInputFiles = open('input_files_RAWSIM.txt').readlines()
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.publishDataName = 'CRAB3_T2tb_AODSIM'

config.Site.storageSite = 'T2_US_UCSD'
config.Site.whitelist = ['T2_US_UCSD']
config.Site.blacklist = ['T2_US_Wisconsin','T2_US_Caltech','T2_US_Purdue','T2_IT_Pisa','T2_IT_Legnaro']
