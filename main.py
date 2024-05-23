from PIL import Image

def resize_image(input_path: str, output_path: str, new_width: int, new_height: int) -> None:
    try:
        with Image.open(input_path) as img:
            resized_img = img.resize((new_width, new_height))
            resized_img.save(output_path)
            print(f"Зображення збережено як {output_path}")
    except Exception as e:
        print(f"Помилка при зміні розміру зображення: {e}")
        
def main() -> None:
    input_path = input("Введіть шлях до початкового зображення: ")
    # input_path = r"C:\Users\Hanashiko\Desktop\resizeImgPyadw\digit.png" 
    # шлях початкового зображення
    output_path = input("Введіть шлях для результатного зображення: ")
    # output_path = r"C:\Users\Hanashiko\Desktop\resizeImgPyadw\result_digit.png"
    # шлях результатного зображення
    new_width = int(input("Введіть нову ширину: "))
    # new_width = 28
    # нова ширина
    new_height = int(input("Введіть нову висоту: "))
    # new_height = 28
    # нова висота
    
    resize_image(input_path, output_path, new_width, new_height)
    
if __name__ == "__main__":
    main()
