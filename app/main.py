from pipeline import extract, load, transform

if __name__ == '__main__':
    data_frame_list = extract.extract_from_excel('data/input')
    print(type(data_frame_list))
    data_frame = transform.concatenate_data_frames(data_frame_list)
    print(type(data_frame))
    load.load_excel(data_frame, 'data/output', 'output')
