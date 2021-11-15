import os.path

from google.cloud import storage
import glob

# upload
def upload_blob(bucket_name, source_file_name, destination_blob_name):

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    try:
        blob.upload_from_filename(source_file_name)
    except:
        blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

# 환경변수
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"D:\workspace\dev\xxxxxxxxxxxxxx.json"

if __name__ == "__main__":
    for dir_num in range(1, 11):
        f = open('log.txt', 'a')
        f.write('########## directory ' + str(dir_num) + ' ##########\n')
        f.close()
        print('directory', dir_num)
        image_list1 = glob.glob("D:\workspace\dev\objects\datasets\\augmented-set\\toupload\\" + str(dir_num) + "\*.jpg")
        image_list2 = glob.glob("D:\workspace\dev\objects\datasets\\augmented-set\\toupload\\" + str(dir_num) + "\*.jpeg")
        image_list = image_list1 + image_list2
        dir_len = len(image_list)
        print(dir_len)
        img_num = 1
        for image in image_list:
            upload_blob(
                bucket_name="xxxxxxxxxxxxxxx",
                source_file_name=image,
                destination_blob_name='images/' + image.split('\\')[-1],
            )
            print('dir ', dir_num, ': ', img_num, '/', dir_len)
            img_num += 1
            if (img_num % 100) == 0 or img_num == dir_len:
                f = open('log.txt', 'a')
                f.write('dir ' + str(dir_num) + ': ' + str(img_num) + '/' + str(dir_len) + '\n')
                f.close()
        f = open('log.txt', 'a')
        f.write('---------- directory ' + str(dir_num) + ' is done ----------\n')
        f.close()
