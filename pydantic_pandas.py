import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date, timedelta
from typing import List, Dict, Optional
from pydantic import BaseModel, Field, validator
import random
import uuid

# Set plotting style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# -------------------- PYDANTIC MODELS --------------------

class ClothingItem(BaseModel):
    """Model for clothing items"""
    item_id: str
    category: str
    subcategory: str
    gender: str
    size: str
    color: str
    material: str
    country_of_origin: str
    
    @validator('category')
    def validate_category(cls, v):
        valid_categories = {'tops', 'bottoms', 'outerwear', 'dresses', 'accessories'}
        if v.lower() not in valid_categories:
            raise ValueError(f"Invalid category: {v}")
        return v.lower()
    
    @validator('gender')
    def validate_gender(cls, v):
        valid_genders = {'men', 'women', 'unisex', 'children'}
        if v.lower() not in valid_genders:
            raise ValueError(f"Invalid gender: {v}")
        return v.lower()


class SalesTransaction(BaseModel):
    """Model for sales transactions"""
    transaction_id: str
    date: date
    item: ClothingItem
    store_id: str
    store_country: str
    store_city: str
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)
    discount_percent: float = Field(ge=0, le=100)
    customer_id: Optional[str] = None
    payment_method: str
    
    @property
    def total_price(self) -> float:
        return round(self.unit_price * self.quantity * (1 - self.discount_percent / 100), 2)
    
    @validator('store_country')
    def validate_country(cls, v):
        asian_countries = {'china', 'japan', 'nepal', 'india', 'singapore', 
                          'thailand', 'vietnam', 'malaysia', 'indonesia', 'philippines'}
        if v.lower() not in asian_countries:
            raise ValueError(f"Country must be in Asia: {v}")
        return v.lower()


class SalesData(BaseModel):
    """Collection of sales transactions"""
    transactions: List[SalesTransaction]
    
    def to_dataframe(self) -> pd.DataFrame:
        """Convert transactions to a pandas DataFrame"""
        data = []
        
        for tx in self.transactions:
            row = {
                # Transaction info
                'transaction_id': tx.transaction_id,
                'date': tx.date,
                'store_id': tx.store_id,
                'store_country': tx.store_country,
                'store_city': tx.store_city,
                'payment_method': tx.payment_method,
                'quantity': tx.quantity,
                'unit_price': tx.unit_price,
                'discount_percent': tx.discount_percent,
                'total_price': tx.total_price,
                'customer_id': tx.customer_id,
                
                # Item info
                'item_id': tx.item.item_id,
                'category': tx.item.category,
                'subcategory': tx.item.subcategory,
                'gender': tx.item.gender,
                'size': tx.item.size,
                'color': tx.item.color,
                'material': tx.item.material,
                'country_of_origin': tx.item.country_of_origin
            }
            data.append(row)
            
        return pd.DataFrame(data)


# -------------------- DATA GENERATION --------------------

def generate_sample_data(num_transactions: int = 1000) -> SalesData:
    """Generate synthetic sales data for Asian clothing markets"""
    
    # Constants for data generation
    COUNTRIES = {
        "china": ["shanghai", "beijing", "guangzhou", "shenzhen", "chengdu"],
        "japan": ["tokyo", "osaka", "kyoto", "fukuoka", "nagoya"],
        "nepal": ["kathmandu", "jiri", "pokhara", "dhangadi", "biratnagar"],
        "india": ["mumbai", "delhi", "bangalore", "chennai", "hyderabad"],
        "singapore": ["central", "east", "west", "north", "south"],
        "thailand": ["bangkok", "chiang mai", "phuket", "pattaya", "krabi"]
    }
    
    CATEGORIES = {
        "tops": ["t-shirt", "shirt", "blouse", "sweater", "hoodie", "polo"],
        "bottoms": ["jeans", "pants", "shorts", "skirt", "leggings"],
        "outerwear": ["jacket", "coat", "blazer", "windbreaker"],
        "dresses": ["casual dress", "formal dress", "evening gown", "sundress"],
        "accessories": ["hat", "scarf", "belt", "bag", "jewelry", "watch"]
    }
    
    GENDERS = ["men", "women", "unisex", "children"]
    COLORS = ["black", "white", "blue", "red", "green", "yellow", "gray", "brown", "pink", "purple"]
    MATERIALS = ["cotton", "polyester", "linen", "wool", "silk", "denim", "leather", "nylon"]
    SIZES = ["XS", "S", "M", "L", "XL", "XXL"]
    PAYMENT_METHODS = ["credit card", "debit card", "cash", "mobile payment", "online wallet"]
    
    # Seasonal effects - certain items sell better in certain months
    SEASONAL_WEIGHTS = {
        # month: (tops, bottoms, outerwear, dresses, accessories)
        1: (0.7, 0.6, 1.5, 0.3, 0.8),    # January: winter
        2: (0.7, 0.6, 1.4, 0.3, 0.8),    # February
        3: (0.8, 0.8, 1.0, 0.8, 0.9),    # March: early spring
        4: (1.0, 1.0, 0.7, 1.2, 1.0),    # April
        5: (1.2, 1.2, 0.5, 1.3, 1.1),    # May: spring
        6: (1.3, 1.3, 0.3, 1.4, 1.2),    # June: early summer
        7: (1.5, 1.4, 0.2, 1.5, 1.3),    # July: summer
        8: (1.4, 1.3, 0.3, 1.4, 1.3),    # August
        9: (1.2, 1.2, 0.7, 1.0, 1.1),    # September: fall
        10: (1.0, 1.1, 1.0, 0.8, 1.0),   # October
        11: (0.9, 0.9, 1.3, 0.5, 0.9),   # November: early winter
        12: (1.0, 0.8, 1.5, 0.6, 1.5)    # December: winter & gifts
    }
    
    # Generate transactions
    transactions = []
    start_date = date(2023, 1, 1)
    end_date = date(2023, 12, 31)
    days_range = (end_date - start_date).days
    
    for _ in range(num_transactions):
        # Create a transaction date with seasonal effects
        random_days = random.randint(0, days_range)
        transaction_date = start_date + timedelta(days=random_days)
        month = transaction_date.month
        
        # Apply seasonal probability to categories
        category_weights = {
            "tops": SEASONAL_WEIGHTS[month][0],
            "bottoms": SEASONAL_WEIGHTS[month][1],
            "outerwear": SEASONAL_WEIGHTS[month][2],
            "dresses": SEASONAL_WEIGHTS[month][3],
            "accessories": SEASONAL_WEIGHTS[month][4]
        }
        
        # Weighted selection of category based on season
        categories = list(category_weights.keys())
        weights = [category_weights[cat] for cat in categories]
        total = sum(weights)
        normalized_weights = [w/total for w in weights]
        category = random.choices(categories, weights=normalized_weights, k=1)[0]
        
        # Select random subcategory and details
        subcategory = random.choice(CATEGORIES[category])
        country = random.choice(list(COUNTRIES.keys()))
        city = random.choice(COUNTRIES[country])
        
        # Create a clothing item
        item = ClothingItem(
            item_id=f"ITEM-{uuid.uuid4().hex[:8].upper()}",
            category=category,
            subcategory=subcategory,
            gender=random.choice(GENDERS),
            size=random.choice(SIZES),
            color=random.choice(COLORS),
            material=random.choice(MATERIALS),
            country_of_origin=random.choice(list(COUNTRIES.keys()))  # Manufacturing country
        )
        
        # Set pricing based on category (different price ranges per category)
        base_prices = {
            "tops": (15, 50),
            "bottoms": (25, 80),
            "outerwear": (50, 200),
            "dresses": (40, 150),
            "accessories": (10, 100)
        }
        price_range = base_prices.get(category, (20, 60))
        unit_price = round(random.uniform(price_range[0], price_range[1]), 2)
        
        # Apply holiday/seasonal sales
        is_holiday_season = month == 12 or month == 1 or month == 7  # Winter sale and summer sale
        discount_prob = 0.6 if is_holiday_season else 0.3
        
        # Maybe apply a discount
        discount = 0
        if random.random() < discount_prob:
            discount = random.choice([10, 15, 20, 25, 30, 40, 50])
        
        # Create the transaction
        transaction = SalesTransaction(
            transaction_id=f"TX-{uuid.uuid4().hex[:10].upper()}",
            date=transaction_date,
            item=item,
            store_id=f"STORE-{country[:2].upper()}{random.randint(1, 99):02d}",
            store_country=country,
            store_city=city,
            quantity=random.randint(1, 5),  # Most people buy 1-5 items
            unit_price=unit_price,
            discount_percent=discount,
            customer_id=f"CUST-{uuid.uuid4().hex[:8].upper()}" if random.random() > 0.2 else None,  # 20% anonymous customers
            payment_method=random.choice(PAYMENT_METHODS)
        )
        
        transactions.append(transaction)
    
    return SalesData(transactions=transactions)


# -------------------- DATA ANALYSIS FUNCTIONS --------------------

def analyze_sales_data(sales_df: pd.DataFrame) -> Dict:
    """Analyze the sales data and return key statistics and insights"""
    
    # Basic statistics
    total_sales = sales_df['total_price'].sum()
    total_transactions = sales_df['transaction_id'].nunique()
    total_items_sold = sales_df['quantity'].sum()
    avg_transaction_value = total_sales / total_transactions
    
    # Convert date to datetime if it's not already
    if not pd.api.types.is_datetime64_any_dtype(sales_df['date']):
        sales_df['date'] = pd.to_datetime(sales_df['date'])
    
    # Add month and quarter for time analysis
    sales_df['month'] = sales_df['date'].dt.month
    sales_df['month_name'] = sales_df['date'].dt.strftime('%B')
    sales_df['quarter'] = sales_df['date'].dt.quarter
    
    # Top selling categories
    category_sales = sales_df.groupby('category').agg(
        total_sales=('total_price', 'sum'),
        units_sold=('quantity', 'sum'),
        avg_price=('unit_price', 'mean')
    ).sort_values('total_sales', ascending=False)
    
    # Sales by country
    country_sales = sales_df.groupby('store_country').agg(
        total_sales=('total_price', 'sum'),
        units_sold=('quantity', 'sum'),
        avg_price=('unit_price', 'mean'),
        transaction_count=('transaction_id', 'nunique')
    ).sort_values('total_sales', ascending=False)
    
    # Monthly trends
    monthly_sales = sales_df.groupby('month').agg(
        total_sales=('total_price', 'sum'),
        units_sold=('quantity', 'sum'),
        transaction_count=('transaction_id', 'nunique')
    ).sort_index()
    
    # Join month names for better readability
    month_names = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April', 
        5: 'May', 6: 'June', 7: 'July', 8: 'August', 
        9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }
    monthly_sales['month_name'] = monthly_sales.index.map(month_names)
    
    # Category performance by month
    category_by_month = sales_df.groupby(['month', 'category']).agg(
        total_sales=('total_price', 'sum')
    ).reset_index().pivot(index='month', columns='category', values='total_sales')
    
    # Discount analysis
    sales_df['discount_bin'] = pd.cut(
        sales_df['discount_percent'], 
        bins=[-0.1, 0.1, 10, 20, 30, 40, 100],
        labels=['No Discount', '1-10%', '11-20%', '21-30%', '31-40%', '41%+']
    )
    
    discount_analysis = sales_df.groupby('discount_bin').agg(
        total_sales=('total_price', 'sum'),
        units_sold=('quantity', 'sum'),
        avg_price=('unit_price', 'mean'),
        transaction_count=('transaction_id', 'nunique')
    )
    
    return {
        'summary': {
            'total_sales': total_sales,
            'total_transactions': total_transactions,
            'total_items_sold': total_items_sold,
            'avg_transaction_value': avg_transaction_value
        },
        'category_sales': category_sales,
        'country_sales': country_sales,
        'monthly_sales': monthly_sales,
        'category_by_month': category_by_month,
        'discount_analysis': discount_analysis
    }


def plot_sales_insights(analysis_results: Dict) -> None:
    """Generate visualizations from the sales analysis"""
    
    # Set up the figure size and style for better readability
    plt.figure(figsize=(14, 8))
    
    # 1. Monthly Sales Trend
    plt.subplot(2, 2, 1)
    monthly_data = analysis_results['monthly_sales']
    plt.plot(monthly_data.index, monthly_data['total_sales'], marker='o', linewidth=2)
    plt.title('Monthly Sales Trend', fontsize=14)
    plt.xlabel('Month')
    plt.ylabel('Total Sales ($)')
    plt.xticks(monthly_data.index, [m[:3] for m in monthly_data['month_name']], rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # 2. Sales by Category
    plt.subplot(2, 2, 2)
    category_data = analysis_results['category_sales']
    category_data['total_sales'].plot(kind='barh', color='skyblue')
    plt.title('Sales by Category', fontsize=14)
    plt.xlabel('Total Sales ($)')
    plt.ylabel('Category')
    plt.grid(True, axis='x', linestyle='--', alpha=0.7)
    
    # 3. Sales by Country
    plt.subplot(2, 2, 3)
    country_data = analysis_results['country_sales']
    country_data['total_sales'].plot(kind='bar', color='lightgreen')
    plt.title('Sales by Country', fontsize=14)
    plt.xlabel('Country')
    plt.ylabel('Total Sales ($)')
    plt.xticks(rotation=45)
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    
    # 4. Discount Impact
    plt.subplot(2, 2, 4)
    discount_data = analysis_results['discount_analysis']
    discount_data['total_sales'].plot(kind='bar', color='salmon')
    plt.title('Impact of Discounts on Sales', fontsize=14)
    plt.xlabel('Discount Range')
    plt.ylabel('Total Sales ($)')
    plt.xticks(rotation=45)
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()
    
    # 5. Category Sales by Month - Heat Map
    plt.figure(figsize=(14, 6))
    category_month_data = analysis_results['category_by_month']
    
    # Need to normalize the data for better visualization
    sns.heatmap(category_month_data, cmap='YlGnBu', annot=True, fmt='.0f', 
                linewidths=.5, cbar_kws={'label': 'Sales ($)'})
    plt.title('Category Sales by Month', fontsize=16)
    plt.ylabel('Month')
    plt.xlabel('Category')
    
    # Replace month numbers with month names
    month_labels = [m[:3] for m in analysis_results['monthly_sales']['month_name']]
    plt.yticks(np.arange(0.5, 12.5), month_labels)
    
    plt.tight_layout()
    plt.show()


# -------------------- MAIN EXECUTION --------------------

def main():
    """Main function to generate and analyze clothing sales data"""
    
    # Generate sample data
    print("Generating synthetic Asian clothing sales data...")
    sales_data = generate_sample_data(num_transactions=2000)
    
    # Convert to pandas DataFrame
    df = sales_data.to_dataframe()
    
    print(f"Generated {len(df)} sales records across {df['store_country'].nunique()} countries")
    
    # Display the first few rows
    print("\nSample data:")
    print(df.head())
    
    # Get basic information about the dataset
    print("\nDataset info:")
    print(f"Shape: {df.shape}")
    print(f"Columns: {', '.join(df.columns)}")
    
    # Analyze the data
    print("\nAnalyzing sales data...")
    analysis_results = analyze_sales_data(df)
    
    # Print summary statistics
    summary = analysis_results['summary']
    print("\n=== Sales Summary ===")
    print(f"Total Sales: ${summary['total_sales']:,.2f}")
    print(f"Total Transactions: {summary['total_transactions']:,}")
    print(f"Total Items Sold: {summary['total_items_sold']:,}")
    print(f"Average Transaction Value: ${summary['avg_transaction_value']:.2f}")
    
    # Print category analysis
    category_sales = analysis_results['category_sales']
    print("\n=== Category Analysis ===")
    print(category_sales)
    
    # Print country analysis
    country_sales = analysis_results['country_sales']
    print("\n=== Country Analysis ===")
    print(country_sales)
    
    # Print monthly trends
    monthly_sales = analysis_results['monthly_sales']
    print("\n=== Monthly Trends ===")
    print(monthly_sales[['total_sales', 'units_sold', 'month_name']])
    
    # Plot insights
    print("\nGenerating visualizations...")
    plot_sales_insights(analysis_results)
    
    # Additional analysis: top selling products by subcategory
    top_subcategories = df.groupby('subcategory').agg(
        total_sales=('total_price', 'sum'),
        units_sold=('quantity', 'sum')
    ).sort_values('total_sales', ascending=False).head(10)
    
    print("\n=== Top Selling Subcategories ===")
    print(top_subcategories)
    
    # Payment method analysis
    payment_analysis = df.groupby('payment_method').agg(
        total_sales=('total_price', 'sum'),
        transaction_count=('transaction_id', 'nunique'),
        avg_transaction=('total_price', lambda x: x.sum() / df.loc[df['payment_method'] == x.name, 'transaction_id'].nunique())
    ).sort_values('total_sales', ascending=False)
    
    print("\n=== Payment Method Analysis ===")
    print(payment_analysis)
    
    print("\nAnalysis complete!")


# Import required for plotting
import numpy as np

if __name__ == "__main__":
    main()