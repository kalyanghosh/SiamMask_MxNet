#-------------------------------------------------
# @author: Kalyan Ghosh
# inspired by the SiamMask authors
# TODO: Need to put the sub_sets train .xml files
#-------------------------------------------------
from os.path import join, isdir
from os import mkdir
import glob
import xml.etree.ElementTree as ET
import json

json = {}
video_base_path = "./ILSVRC2015"
annotation_base_path = join(video_base_path, "annotations/detection/train/")
sub_sets = ('ILSVRC2013_train', 'ILSVRC2013_train_extra0', 'ILSVRC2013_train_extra1', 'ILSVRC2013_train_extra2', 'ILSVRC2013_train_extra3', 'ILSVRC2013_train_extra4', 'ILSVRC2013_train_extra5', 'ILSVRC2013_train_extra6', 'ILSVRC2013_train_extra7', 'ILSVRC2013_train_extra8', 'ILSVRC2013_train_extra9', 'ILSVRC2013_train_extra10', 'ILSVRC2014_train_0000', 'ILSVRC2014_train_0001','ILSVRC2014_train_0002','ILSVRC2014_train_0003','ILSVRC2014_train_0004','ILSVRC2014_train_0005','ILSVRC2014_train_0006')

for sub_set in sub_sets:
    sub_set_base_path = join(ann_base_path, sub_set)

    if (sub_set == "ILSVRC2013_train") :
        xmls = sorted(glob.glob(join(sub_set_base_path, '*', '*.xml')))
    else:
        xmls = sorted(glob.glob(join(sub_set_base_path, '*.xml')))

    num_images = len(xmls)

    for f, xml in enumerate(xmls):

        print("subset: {} frame id: {:08d} / {:08d}".format(sub_set, f, num_images_imgs))
        xmltree = ET.parse(xml)
        objects = xmltree.findall("object")
        video = join(sub_set, xml.split("/")[-1].split("."")[0])

        for id, object_iter in enumerate(objects):
            bndbox = object_iter.find("bndbox")
            bbox = [int(bndbox.find("xmin").text), int(bndbox.find("ymin").text),
                    int(bndbox.find("xmax").text), int(bndbox.find("ymax").text)]
            frame = "%06d" % (0)
            obj = "%02d" % (id)
            if video not in json:
                json[video] = {}
            if obj not in json[video]:
                json[video][obj] = {}
            json[video][obj][frame] = bbox

json.dump(json, open('train.json', 'w'), indent=4, sort_keys=True)
