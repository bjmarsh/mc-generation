# mc-generation

Collection of crab3/cmssw config files for generating MINIAODSIM monte-carlo, starting with an LHE file.
To use, you'll have to edit the name of your desired LHE file in crab_config_LHEtoGENSIM.py and LHEtoGENSIM_cfg.py. 
You can further edit the config files to get your desired output file and dataset names, as well as the desired
number of events to simulate (choose njobs and nevents/job in the crab config file).

Once you have made the desired edits, submit the crab config files one at a time to with crab submit. You have to wait
until one stage has completely finished running before submitting the next.

A sample LHE file for T2tb events with 425/230/225 stop/chargino/LSP masses is at /hadoop/cms/store/user/bemarsh/SMS-T2tb_2J_mStop-425_mChgno-230_mLSP-2225_MCRUN2_74_V9-v1/merged_425.lhe
