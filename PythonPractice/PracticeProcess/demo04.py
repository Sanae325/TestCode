'''
多任务文件夹copy
'''
import os
import multiprocessing

def copy_file(q, file_name, old_folder_name, new_folder_name):
    '''完成文件的复制'''
    old_f = open(old_folder_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()

    # 如果拷贝完了文件，那么就向队列中写入一个消息，表示已经完成
    q.put(file_name)


def main():
    # 获取用户要copy的文件夹的名字
    old_folder_name = input("请输入要copy的文件夹的名字：")

    # 创建一个新的文件夹
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(new_folder_name)
    except:
        pass
    
    # 获取文件夹的所有的待copy的文件名字 listdir()
    file_names = os.listdir(old_folder_name)

    # 创建进程池
    po = multiprocessing.Pool(3)

    # 创建一个队列
    q = multiprocessing.Manager().Queue()

    # 向进程池中添加copy文件的任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(q, file_name, old_folder_name, new_folder_name))
    
    po.close()

    all_file_num = len(file_names) # 所有文件的个数
    copy_ok_num = 0

    while True:
        file_name = q.get()
        copy_ok_num += 1
        print("\r拷贝的进度为：%.2f %%" % (copy_ok_num*100 / all_file_num), end="")
        if copy_ok_num >= all_file_num:
            break
    print()


if __name__ == "__main__":
    main()