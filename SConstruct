# -*- python -*-
#
# Setup our environment
#
import glob
import lsst.SConsUtils as scons

env = scons.makeEnv("afwdata",
                    r"$HeadURL$",
                    [])

Alias("install", [env.Install(env['prefix'], glob.glob("*.fits")),
                  env.Install(env['prefix'], "CFHT"),
                  env.InstallEups(env['prefix'] + "/ups", glob.glob("ups/*.table"))])


scons.CleanTree(r"*~ core *.so *.os *.o")

env.Declare()

env.Help("""
Test data for lsst/fw
""")

