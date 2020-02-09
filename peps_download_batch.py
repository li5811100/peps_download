# !/usr/bin/env python
# -*- coding: utf-8 -*-


import subprocess
import time
import tempfile
import glob
import os


def main():
    logDir = "peps.log"

    separator = ' '

    out_folder = "/media/ivan/CapitalMapping"
    out_folder = "/media/ivan/6T/T51RUQ-12-Yanrz/NDVI"
    out_folder = "/media/ivan/6T"
    out_folder = "/media/ivan/6T/zjm/2019_zjm_high"
    out_folder = "/media/ivan/6T"

    print(out_folder)
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)

    data_dir = "/media/ivan/2T/PycharmProjects/peps_download-master/T50TMK"
    data_dir = "/media/ivan/2T/PycharmProjects/peps_download-master/mengnei-zhongba-2018"
    data_dir = "/media/ivan/2T/PycharmProjects/peps_download-master/xiongxian_2019_4jing"
    data_dir = "/media/ivan/2T/PycharmProjects/peps_download-master/T50SMJ-20190901-20191124"
    data_dir = "/media/ivan/2T/PycharmProjects/peps_download-master/T51SUR-2019-GOOD"
    data_dir = "/media/ivan/2T/PycharmProjects/peps_download-master/20191101-20191130-T50TMK"
    # data_dir = "/media/ivan/2T/PycharmProjects/peps_download-master/T51SUR-2017-2018-GOOD"
    # data_dir = "/media/ivan/2T/PycharmProjects/peps_download-master/20190907-20191030-T50SMK"
    # data_dir = "/media/ivan/2T/PycharmProjects/peps_download-master/T51RUQ-201706-201804-GOOD-12-Yanrz"
    data_dir = "/media/ivan/2T/PycharmProjects/peps_download-master/T51RUQ-20170101-20191220-GOOD"


    capitals = glob.glob( data_dir + "/*.csv")
    if capitals == []:
        print("no file founded...")
        return

    for capital in capitals:
        if not os.path.isdir(capital):
            out_folder_2 = out_folder + '/' + capital.split('/')[-1].split('.')[0]
            if not os.path.exists(out_folder_2):
                os.mkdir(out_folder_2)
            f = open(capital)
            files = f.read()
            files = files.split('\n')
            imgs = [ x for x in files]
            print(files)
            hypes = []

            for img in imgs:
                if img == '': continue
                hype = []
                tile = img.split(separator)[0]
                dateb = img.split(separator)[1]
                datee = img.split(separator)[2]
                out_p = out_folder_2 #+'/'+ tile
                print(out_p)
                if not os.path.exists(out_p):
                    os.mkdir(out_p)
                hype.append(dateb)
                hype.append(datee)
                hype.append(tile)
                hype.append(out_p)
                hypes.append(hype)

            print('totally ', len(hypes), ' jobs are to be conducted')
            # for i in hypes:
            #     print(i,"\n")
            for i in range(len(hypes)):  # "/media/cr/data_y/task-qy-fcn/res"


                m_hypes = "python peps_download.py -c S2ST -p S2MSI1C -a peps.txt" + " -d " + hypes[i][0] + " -f " + hypes[i][1]  + " --t=" + hypes[i][2] \
                            + ' --write_dir ' + hypes[i][3]

                f = open(logDir, 'a+')

                mt = time.asctime(time.localtime(time.time()))

                f.write(mt)
                f.write('\n')
                f.write(m_hypes + '\n')

                try:
                    print(m_hypes)
                    # pp=subprocess.Popen(m_hypes,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
                    # 得到一个临时文件对象， 调用close后，此文件从磁盘删除
                    out_temp = tempfile.TemporaryFile(mode='w+')
                    # 获取临时文件的文件号
                    fileno = out_temp.fileno()
                    # 执行外部shell命令， 输出结果存入临时文件中
                    pp = subprocess.Popen(m_hypes, shell=True, stdin=fileno, stdout=fileno)
                    pp.wait()
                    print(i + 1, " in ", int(len(hypes)), "finished")
                    print("\n")
                except Exception as e:
                    fr = open(logDir, 'a+')
                    mt = time.asctime(time.localtime(time.time()))
                    f.write(mt)
                    f.write('\n')
                    fr.write(m_hypes + '\n')
                    fr.write(e.message + '\n')
                    fr.write('\n')
                    fr.close()
                finally:
                    if out_temp:
                        out_temp.close()

                mt = time.asctime(time.localtime(time.time()))
                f.write(mt)
                f.write('\n')
                f.write('\n')
                f.close()


if __name__ == '__main__':
    main()
