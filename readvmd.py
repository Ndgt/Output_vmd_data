from vmd import (VMD_HEADER, VMD_MOTION_COUNT, VMD_MOTION, VMD_SKIN_COUNT, VMD_SKIN,
                 VMD_CAMERA_COUNT, VMD_CAMERA, VMD_LIGHT_COUNT, VMD_LIGHT,
                 VMD_SELF_SHADOW, VMD_SELF_SHADOW_COUNT,
                 vmdread, vmdoutput)
import os
import argparse

# Set up argument parser
parser = argparse.ArgumentParser()
parser.add_argument("filepath", help="Path to the input file")
args = parser.parse_args()

# Read the VMD
vmdfilepath = args.filepath

if not os.path.exists(vmdfilepath):
    print("File does not exist")

else:
    with open(vmdfilepath, "rb") as file, \
         open("vmd_data.txt", "w", encoding="utf-8") as result:
        
        # title
        vmdoutput(result, "vmd file name : " + vmdfilepath)
        
        # Header
        vmd_header = VMD_HEADER(
            VmdHeader=vmdread(file, 30, "30s"),
            VmdModelName=vmdread(file, 20, "20s")
            )
        vmdoutput(result, "\n--- Header ---")
        vmdoutput(result, vmd_header.VmdHeader)
        vmdoutput(result, vmd_header.VmdModelName)

        # Motion Data Count
        vmd_motion_count = VMD_MOTION_COUNT(Count=vmdread(file, 4, "I"))
        vmdoutput(result, "\n--- Motion Data Count ---")
        vmdoutput(result, str(vmd_motion_count.Count))

        # Motion Data
        vmdoutput(result, "\n--- Motion Data ---")
        for _count in range(vmd_motion_count.Count):
            vmd_motion = VMD_MOTION(
                BoneName=vmdread(file, 15, "15s"),
                FrameNo=vmdread(file, 4, "I"),
                Location=vmdread(file, 12, "3f"),
                Rotation=vmdread(file, 16, "4f"),
                Interpolation=vmdread(file, 64, "64B")
            )            
            for i in range(len(vmd_motion)):
                vmdoutput(result, vmd_motion)
                # vmdoutput(result, vmd_motion[i]) # output each data

            vmdoutput(result, "")

        # Skin Data Count
        vmd_skin_count = VMD_SKIN_COUNT(Count=vmdread(file, 4, "I"))
        vmdoutput(result, "\n--- Skin Data Count ---")
        vmdoutput(result, str(vmd_skin_count.Count))

        # Skin Data
        vmdoutput(result, "\n--- Skin Data ---")
        for _count in range(vmd_skin_count.Count):
            vmd_skin = VMD_SKIN(
                SkinName=vmdread(file, 15, "15s"),
                FrameNo=vmdread(file, 4, "I"),
                Weight=vmdread(file, 4, "f")
            )
            for i in range(len(vmd_skin)):
                vmdoutput(result, vmd_skin)
                # vmdoutput(result, vmd_skin[i]) # output each data

            vmdoutput(result, "")

        # Camera Data Count
        vmd_camera_count = VMD_CAMERA_COUNT(Count=vmdread(file, 4, "I"))
        vmdoutput(result, "\n--- Camera Data Count ---")
        vmdoutput(result, str(vmd_camera_count.Count))

        # Camera Data
        vmdoutput(result, "\n--- Camera Data ---")
        for _count in range(vmd_camera_count.Count):
            vmd_camera = VMD_CAMERA(
                FrameNo=vmdread(file, 4, "I"),
                Length=vmdread(file, 4, "f"),
                Location=vmdread(file, 12, "3f"),
                Rotation=vmdread(file, 12, "3f"),
                Interpolation=vmdread(file, 24, "24B"),
                ViewingAngle=vmdread(file, 4, "I"),
                Perspective=vmdread(file, 1, "B")
            )
            for i in range(len(vmd_camera)):
                vmdoutput(result, vmd_camera)
                # vmdoutput(result, vmd_camera[i]) # output each data

            vmdoutput(result, "")

        # Light Data Count
        vmd_light_count = VMD_LIGHT_COUNT(Count=vmdread(file, 4, "I"))
        vmdoutput(result, "\n--- Light Data Count ---")
        vmdoutput(result, str(vmd_light_count.Count))

        # Light Data
        vmdoutput(result, "\n--- Light Data ---")
        for _count in range(vmd_light_count.Count):
            vmd_light = VMD_LIGHT(
                FrameNo=vmdread(file, 4, "I"),
                RGB=vmdread(file, 12, "3f"),
                Location=vmdread(file, 12, "3f"),
            )
            for i in range(len(vmd_light)):
                vmdoutput(result, vmd_light)
                # vmdoutput(result, vmd_light[i]) # output each data

            vmdoutput(result, "")

        # Self Shadow Data Count
        vmd_self_shadow_count = VMD_SELF_SHADOW_COUNT(Count=vmdread(file, 4, "I"))
        vmdoutput(result, "\n--- Self Shadow Data Count ---")
        vmdoutput(result, str(vmd_self_shadow_count.Count))

        # Self Shadow Data
        vmdoutput(result, "\n--- Self Shadow Data ---")
        for _count in range(vmd_self_shadow_count.Count):
            vmd_self_shadow = VMD_SELF_SHADOW(
                FrameNo=vmdread(file, 4, "I"),
                Mode=vmdread(file, 1, "B"),
                Distance=vmdread(file, 4, "f")
            )
            for i in range(len(vmd_self_shadow)):
                vmdoutput(result, vmd_self_shadow)
                # vmdoutput(result, vmd_self_shadow[i]) # output each data

            vmdoutput(result, "")