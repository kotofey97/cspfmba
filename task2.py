import os
from glob import glob

labels_dir = "/tmp/labels"
os.makedirs(labels_dir, exist_ok=True)
labels = {
    "label1": ["1image.JPG", "2.jpeg", "2.json", "1image.json", "3.jpg"],
    "label2": ["1.jpg", "1.json", "2.json", "3.json"],
    "label3": ["15.png", "15.json", "16.json", "16.jpg", "1.PNG", "1.JSON"],
    "label4": ["1.png", "1.txt", "2.txt", ],
}

for label in labels:
    label_path = os.path.join(labels_dir, label)
    os.makedirs(label_path, exist_ok=True)
    for item in labels[label]:
        open(os.path.join(label_path, item), 'a').close()
    print(f"{label_path} {os.listdir(label_path)}")
open(os.path.join(labels_dir, "test.txt"), 'a').close()


def func(dict):
    EXTENSION = ['png', 'jpg', 'json', 'jpeg']
    answer = []
    for label in labels:        
        for idx in range(1,5):
            if label == f'label{idx}':
                correct_dict = {f'label{idx}': []}
                for item in labels[label]:
                    main_dir = correct_dict[f'label{idx}']
                    if item.split('.')[-1].lower() not in EXTENSION:
                        break
                    if len(main_dir) == 0:
                        main_dir.append([f'{labels_dir}/label{idx}/{item}'])
                    else:
                        for number_list in range(len(main_dir)):
                            b = False
                            if item.split('.')[0] in main_dir[number_list][0].split('/')[4]:
                                main_dir[number_list].append(f'{labels_dir}/label{idx}/{item}')
                                b = True
                                break
                        if b is False:
                            main_dir.append([f'{labels_dir}/label{idx}/{item}'])
                for number_list in reversed(main_dir):
                    if len(number_list) == 1:
                        main_dir.remove(number_list)
                if main_dir != []:
                    answer.append(correct_dict)
    return answer


print(func(labels))
