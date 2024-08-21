import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
data = pd.read_csv('C:/Users/ADMIN/PycharmProjects/pythonProject1/pythonProject/data/data-pt.csv')


print("Giá trị thiếu trong từng cột:")
print(data.isnull().sum())

data = data.dropna()

## Chuyển đổi kiểu dữ liệu
# Đảm bảo các cột có kiểu dữ liệu phù hợp
data['Previous Purchases'] = pd.to_numeric(data['Previous Purchases'], errors='coerce')
data['Purchase Amount (USD)'] = pd.to_numeric(data['Purchase Amount (USD)'], errors='coerce')

# Kiểm tra lại các kiểu dữ liệu
print("\nKiểu dữ liệu của từng cột:")
print(data.dtypes)

# Nếu có cần thiết, làm sạch dữ liệu khác như loại bỏ ký tự không hợp lệ, xử lý giá trị bất thường, v.v.

# **Phân Tích Mô Tả**

# Xem các thông tin tổng quan
print("\nThông tin tổng quan về dữ liệu:")
print(data.info())
print(data.describe(include='all'))

# Số lượng khách hàng duy nhất
unique_customers = data['Customer ID'].nunique()
print(f'\nSố lượng khách hàng duy nhất: {unique_customers}')

# Phân phối độ tuổi của khách hàng
age_distribution = data['Age'].describe()
print('\nPhân phối độ tuổi:')
print(age_distribution)

# Vẽ biểu đồ phân phối độ tuổi
plt.figure(figsize=(10, 6))
data['Age'].hist(bins=10, edgecolor='black')
plt.title('Phân phối độ tuổi của khách hàng')
plt.xlabel('Tuổi')
plt.ylabel('Số lượng khách hàng')
plt.show()

# Tỷ lệ giữa nam và nữ
gender_distribution = data['Gender'].value_counts()
print('\nTỷ lệ giới tính:')
print(gender_distribution)

# Vẽ biểu đồ phân phối giới tính
plt.figure(figsize=(8, 6))
gender_distribution.plot(kind='pie', autopct='%1.1f%%')
plt.title('Tỷ lệ giới tính của khách hàng')
plt.ylabel('')
plt.show()

# Các sản phẩm được mua nhiều nhất
item_distribution = data['Item Purchased'].value_counts()
print('\nSản phẩm phổ biến:')
print(item_distribution.head(10))

# Vẽ biểu đồ sản phẩm phổ biến
plt.figure(figsize=(12, 8))
item_distribution.head(10).plot(kind='bar')
plt.title('Top 10 sản phẩm phổ biến')
plt.xlabel('Sản phẩm')
plt.ylabel('Số lượng')
plt.xticks(rotation=90)
plt.show()

# Các danh mục sản phẩm phổ biến
category_distribution = data['Category'].value_counts()
print('\nPhân phối danh mục sản phẩm:')
print(category_distribution)

# Vẽ biểu đồ phân phối danh mục sản phẩm
plt.figure(figsize=(10, 6))
category_distribution.plot(kind='bar')
plt.title('Phân phối danh mục sản phẩm')
plt.xlabel('Danh mục')
plt.ylabel('Số lượng')
plt.xticks(rotation=45)
plt.show()

# Tổng doanh thu và phân phối số tiền mua hàng
purchase_amount_stats = data['Purchase Amount (USD)'].describe()
print('\nPhân phối số tiền mua hàng:')
print(purchase_amount_stats)

# Vẽ biểu đồ phân phối số tiền mua hàng
plt.figure(figsize=(10, 6))
data['Purchase Amount (USD)'].hist(bins=30, edgecolor='black')
plt.title('Phân phối số tiền mua hàng')
plt.xlabel('Số tiền (USD)')
plt.ylabel('Số lượng giao dịch')
plt.show()

# Phân phối theo địa điểm
location_distribution = data['Location'].value_counts()
print('\nPhân phối địa điểm:')
print(location_distribution)

# Vẽ biểu đồ phân phối địa điểm
plt.figure(figsize=(12, 8))
location_distribution.plot(kind='bar')
plt.title('Phân phối địa điểm')
plt.xlabel('Địa điểm')
plt.ylabel('Số lượng')
plt.xticks(rotation=90)
plt.show()

# Phân phối kích cỡ của sản phẩm
size_distribution = data['Size'].value_counts()
print('\nPhân phối kích cỡ:')
print(size_distribution)

# Vẽ biểu đồ phân phối kích cỡ
plt.figure(figsize=(10, 6))
size_distribution.plot(kind='bar')
plt.title('Phân phối kích cỡ sản phẩm')
plt.xlabel('Kích cỡ')
plt.ylabel('Số lượng')
plt.show()

# Phân phối màu sắc
color_distribution = data['Color'].value_counts()
print('\nPhân phối màu sắc:')
print(color_distribution)

# Vẽ biểu đồ phân phối màu sắc
plt.figure(figsize=(12, 8))
color_distribution.plot(kind='bar')
plt.title('Phân phối màu sắc sản phẩm')
plt.xlabel('Màu sắc')
plt.ylabel('Số lượng')
plt.xticks(rotation=90)
plt.show()

# Phân phối theo mùa
season_distribution = data['Season'].value_counts()
print('\nPhân phối theo mùa:')
print(season_distribution)

# Vẽ biểu đồ phân phối theo mùa
plt.figure(figsize=(10, 6))
season_distribution.plot(kind='bar')
plt.title('Phân phối theo mùa')
plt.xlabel('Mùa')
plt.ylabel('Số lượng')
plt.show()

# Phân phối đánh giá sản phẩm
review_rating_distribution = data['Review Rating'].value_counts().sort_index()
print('\nPhân phối đánh giá sản phẩm:')
print(review_rating_distribution)

# Vẽ biểu đồ phân phối đánh giá
plt.figure(figsize=(10, 6))
review_rating_distribution.plot(kind='bar')
plt.title('Phân phối đánh giá sản phẩm')
plt.xlabel('Đánh giá')
plt.ylabel('Số lượng')
plt.show()

# Tỷ lệ đăng ký
subscription_distribution = data['Subscription Status'].value_counts()
print('\nTỷ lệ đăng ký:')
print(subscription_distribution)

# Vẽ biểu đồ tỷ lệ đăng ký
plt.figure(figsize=(8, 6))
subscription_distribution.plot(kind='pie', autopct='%1.1f%%')
plt.title('Tỷ lệ đăng ký của khách hàng')
plt.ylabel('')
plt.show()

# Phân phối phương thức thanh toán
payment_method_distribution = data['Payment Method'].value_counts()
print('\nPhân phối phương thức thanh toán:')
print(payment_method_distribution)

# Vẽ biểu đồ phân phối phương thức thanh toán
plt.figure(figsize=(10, 6))
payment_method_distribution.plot(kind='bar')
plt.title('Phân phối phương thức thanh toán')
plt.xlabel('Phương thức thanh toán')
plt.ylabel('Số lượng')
plt.show()

# Phân phối loại giao hàng
shipping_type_distribution = data['Shipping Type'].value_counts()
print('\nPhân phối loại giao hàng:')
print(shipping_type_distribution)

# Vẽ biểu đồ phân phối loại giao hàng
plt.figure(figsize=(10, 6))
shipping_type_distribution.plot(kind='bar')
plt.title('Phân phối loại giao hàng')
plt.xlabel('Loại giao hàng')
plt.ylabel('Số lượng')
plt.show()

# Tỷ lệ áp dụng giảm giá
discount_applied_distribution = data['Discount Applied'].value_counts()
print('\nTỷ lệ áp dụng giảm giá:')
print(discount_applied_distribution)

# Vẽ biểu đồ tỷ lệ áp dụng giảm giá
plt.figure(figsize=(8, 6))
discount_applied_distribution.plot(kind='pie', autopct='%1.1f%%')
plt.title('Tỷ lệ áp dụng giảm giá')
plt.ylabel('')
plt.show()

# Tỷ lệ sử dụng mã khuyến mãi
promo_code_used_distribution = data['Promo Code Used'].value_counts()
print('\nTỷ lệ sử dụng mã khuyến mãi:')
print(promo_code_used_distribution)

# Vẽ biểu đồ tỷ lệ sử dụng mã khuyến mãi
plt.figure(figsize=(8, 6))
promo_code_used_distribution.plot(kind='pie', autopct='%1.1f%%')
plt.title('Tỷ lệ sử dụng mã khuyến mãi')
plt.ylabel('')
plt.show()

