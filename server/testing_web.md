**Node.js Code Snippet**

```javascript
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');

  const productData = await page.evaluate(() => {
    const products = document.querySelectorAll('.product');
    const data = [];
    products.forEach((product) => {
      data.push({
        name: product.querySelector('.product-name').textContent,
        description: product.querySelector('.product-description').textContent,
        price: product.querySelector('.product-price').textContent,
        images: [...product.querySelectorAll('.product-image')].map((image) => image.src),
        reviews: [...product.querySelectorAll('.product-review')].map((review) => review.textContent),
      });
    });
    return data;
  });

  const categoryData = await page.evaluate(() => {
    const categories = document.querySelectorAll('.category');
    const data = [];
    categories.forEach((category) => {
      data.push({
        name: category.querySelector('.category-name').textContent,
        subcategories: [...category.querySelectorAll('.subcategory')].map((subcategory) => subcategory.textContent),
      });
    });
    return data;
  });

  const customerData = await page.evaluate(() => {
    const customers = document.querySelectorAll('.customer');
    const data = [];
    customers.forEach((customer) => {
      data.push({
        name: customer.querySelector('.customer-name').textContent,
        email: customer.querySelector('.customer-email').textContent,
        address: customer.querySelector('.customer-address').textContent,
        purchaseHistory: [...customer.querySelectorAll('.purchase-history')].map((purchase) => purchase.textContent),
      });
    });
    return data;
  });

  const salesData = await page.evaluate(() => {
    const sales = document.querySelectorAll('.sale');
    const data = [];
    sales.forEach((sale) => {
      data.push({
        orderDate: sale.querySelector('.order-date').textContent,
        orderNumber: sale.querySelector('.order-number').textContent,
        productPurchased: sale.querySelector('.product-purchased').textContent,
        quantity: sale.querySelector('.quantity').textContent,
        price: sale.querySelector('.price').textContent,
      });
    });
    return data;
  });

  const competitorData = await page.evaluate(() => {
    const competitors = document.querySelectorAll('.competitor');
    const data = [];
    competitors.forEach((competitor) => {
      data.push({
        name: competitor.querySelector('.competitor-name').textContent,
        productData: [...competitor.querySelectorAll('.product-data')].map((product) => product.textContent),
        pricing: [...competitor.querySelectorAll('.pricing')].map((price) => price.textContent),
        promotions: [...competitor.querySelectorAll('.promotions')].map((promotion) => promotion.textContent),
      });
    });
    return data;
  });

  await browser.close();

  return {
    productData,
    categoryData,
    customerData,
    salesData,
    competitorData,
  };
})();
```

**Next.js Code Snippet**

```javascript
import { useEffect, useState } from 'react';
import axios from 'axios';

const EcommerceData = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get('https://example.com/api/data');
      setData(response.data);
    };

    fetchData();
  }, []);

  return (
    <div>
      {data && (
        <>
          <h1>Product Data</h1>
          <ul>
            {data.productData.map((product) => (
              <li key={product.name}>
                {product.name} - {product.price}
              </li>
            ))}
          </ul>

          <h1>Category Data</h1>
          <ul>
            {data.categoryData.map((category) => (
              <li key={category.name}>
                {category.name} - {category.subcategories.join(', ')}
              </li>
            ))}
          </ul>

          <h1>Customer Data</h1>
          <ul>
            {data.customerData.map((customer) => (
              <li key={customer.name}>
                {customer.name} - {customer.email}
              </li>
            ))}
          </ul>

          <h1>Sales Data</h1>
          <ul>
            {data.salesData.map((sale) => (
              <li key={sale.orderNumber}>
                {sale.orderDate} - {sale.productPurchased} - {sale.quantity} - {sale.price}
              </li>
            ))}
          </ul>

          <h1>Competitor Data</h1>
          <ul>
            {data.competitorData.map((competitor) => (
              <li key={competitor.name}>
                {competitor.name} - {competitor.productData.join(', ')} - {competitor.pricing.join(', ')} - {competitor.promotions.join(', ')}
              </li>
            ))}
          </ul>
        </>
      )}
    </div>
  );
};

export default EcommerceData;
```

**Test Cases**

**Functional Testing**

* Verify that all product data is displayed correctly.
* Verify that all category data is displayed correctly.
* Verify that all customer data is displayed correctly.
* Verify that all sales data is displayed correctly.
* Verify that all competitor data is displayed correctly.

**Performance Testing**

* Measure the time it takes for the page to load.
* Measure the time it takes for the data to be displayed.
* Measure the time it takes for the user to interact with the page.

**Compatibility Testing**

* Test the website on different browsers (e.g., Chrome, Firefox, Safari).
* Test the website on different devices (e.g., desktop, laptop, mobile).
* Test the website on different screen sizes.

**Bug Fixes**

* Fix any bugs or issues that are discovered during testing.

**Test Report**

* Document the test results and prepare a test report with recommendations.

**Recommendations**

* Recommend any improvements that can be made to the website.
* Recommend any additional testing that should be performed.