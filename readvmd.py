from vmd import*
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
        vmdoutput(result, "\n--- Motion Count ---")
        vmdoutput(result, "Motion Count :" + str(vmd_motion_count.Count))

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

        # Facial Animation Data Count
        vmd_skin_count = VMD_SKIN_COUNT(Count=vmdread(file, 4, "I"))
        vmdoutput(result, "\n--- Skin Count ---")
        vmdoutput(result, "Skin Count : " + str(vmd_skin_count.Count))

        # Facial Animation Data
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