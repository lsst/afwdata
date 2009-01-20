# -*- python -*-
#
# Setup our environment
#
import glob, os
import lsst.SConsUtils as scons

env = scons.makeEnv("afwdata",
                    r"$HeadURL$",
                    [])

Alias("install", [env.Install(env['prefix'], glob.glob("*.fits")),
                  env.Install(os.path.join(env['prefix'], "CFHT", "D4"),
                              glob.glob(os.path.join("CFHT", "D4", "*.fits"))),
                  env.Install(os.path.join(env['prefix'], "Statistics"),
                              glob.glob(os.path.join("Statistics", "*.fits"))),
                  env.InstallEups(env['prefix'] + "/ups", glob.glob("ups/*.table"))])

scons.CleanTree(r"*~ core *.so *.os *.o")

env.Declare()

env.Help("""
Test data for lsst/fw
""")
