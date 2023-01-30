# Elite Novo Force - ANT+ Virtual Power Meter

## Overview

This project is a fork of [dhague](https://github.com/dhague)/ **[vpower](https://github.com/dhague/vpower)**.

It implements "virtual power" for [Elite Novo Force](https://www.elite-it.com/en/products/home-trainers/classic-trainers/novo-force) (8 resistance levels) using an ANT+  speed sensor.

The calculated power is broadcasted as such on ANT+ so that any head unit or app (e.g. Zwift) will see it as a power meter.

**Note:** Zwift claims they support the Elite Novo Force however, as stated by many users on [Zwift forum](https://forums.zwift.com/t/new-settings-for-elite-novo-force/159201), the power is over estimated and limited to Level 3. This project allows the use of the full set of resistance levels.

## Introduction
Many turbos, such as the Elite Novo Force have well-known and consistent power curves which make it possible to calculate the power from speed.
This concept is used in several applications (Zwift, Golden Cheetah, TrainerRoad, Sufferfest) to allow the user to 
behave as if they had a power meter. 

This is great, up to a point. One issue is that the calculated power is not shown on the user's bike computer, but only 
in the app (except for TrainerRoad). Another issue is that not all apps support all trainers. Even when a turbo is supported, the calculated power may differ from a rider's power meter by as much as  5-10% - this is highly significant when doing intervals in the region of threshold or VO2max.

This project is designed to be run on any computer or Raspberry Pi with an ANT+ stick plugged in, and will broadcast the calculated 
power over ANT+ so that bike computers and apps will see it as a regular ANT+ power meter. The project is designed to be
open-source.

**Important**: To use this project with Zwift or any other app, a second ANT+ USB Stick is necessary because the first USB Stick will be locked by this project and not accessible to other software. If you plan to broadcast only the power to an head unit (e.g. Garmin Edge) only one ANT+ USB Stick is necessary.

## Running on Windows

1. Download and install Python here: https://www.python.org/downloads/windows/

2. Install the ANT stick, it can be easily done using [Zadig](https://zadig.akeo.ie/) or [Wahoo drivers](https://support.wahoofitness.com/hc/en-us/articles/360021559679-Installing-ANT-drivers).

3. Download this repository, unzip and run **Install.bat**

    https://github.com/carlosteixeiraXXX/vpower-elite-novo-force/archive/refs/heads/master.zip

4. Select the desired resistance level, wheel circumference, etc. in vpower.cfg

    `power_calculator = `

    `wheel_circumference = `

5. Run to the program open file **Run.bat**


You should see something like this:

    Power meter ANT+ ID: 37127
    Starting ANT node
    Starting speed sensor
    Using Level1
    Starting power meter
    Main wait loop
    Power: x W

