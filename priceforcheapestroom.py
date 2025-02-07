import io
import os

def main():

    my_path = "D:\abc"
    csv_file = "cap_rooms.csv"
    md_file = "cap_rooms.md"
    csv_file_path = os.path.join(my_path,csv_file)
    md_file_path = os.path.join(my_path, md_file)

    with open(md_file_path,'r',encoding='utf-8') as f:
        md_content = f.read()
    df = pd.read_csv(csv_file_path)
    result = df.groupby('city')["price"].agg(cheapest = 'min', costlist ='max').reset_index()
    print(result)
