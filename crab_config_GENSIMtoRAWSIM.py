from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'T2bw_RAWSIM'
config.General.workArea = 'tasks'
config.General.transferOutputs = True
config.General.transferLogs = True


config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'GENSIMtoRAWSIM_cfg.py'

## use this to run over unpublished files. text file should be a line-by-line list of files
#config.Data.primaryDataset = 'SMS-T2tb_2J_mStop-425_mChgno-230_mLSP-2225_MCRUN2_74_V9-v1'
#config.Data.userInputFiles = open('input_files_GENSIM.txt').readlines()

## use this to run over user-published datasets
config.Data.inputDataset = '/SMS-T2bw_2J_mStop-650_mLSP-325_x-075_MCRUN2_74_V9-v1/bemarsh-CRAB3_T2bw_GENSIM-d7502674d91a720139b41abe5019baad/USER'
config.Data.inputDBS = 'phys03'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
config.Data.publication = True
config.Data.publishDataName = 'CRAB3_T2bw_RAWSIM'

config.Site.storageSite = 'T2_US_UCSD'
#config.Site.whitelist = ['T2_US_UCSD']
#config.Site.blacklist = ['T2_US_Wisconsin']
