import csv

try:
    best_selling_book = []
    with open('BestSeller.csv','r',encoding='utf8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)
        max_sales = 0.0
        
        for row in csv_reader:
            current_sales = float(row[4])
            if current_sales > max_sales:
                max_sales = current_sales
                best_selling_book = row
    
    with open('BestBookInfo.csv','w',encoding='utf8',newline='') as file:
        csv_reader = csv.writer(file)
        csv_reader.writerow(best_selling_book)

            

except Exception as e:
    print(f'Ocurrio un error inesperado: {e}')