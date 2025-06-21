# ✈️ Airline Manager
This is a custom application built using the Frappe Framework to manage both Airplane Operations and Shop Management. It is designed to handle flight scheduling, airplane and crew management, passenger data, as well as airport or in-flight shop inventory, sales, and transactions.

# 🌟 Key Features
# ✈️ Airplane Management
- Manage airplane details (model, capacity, status)
- Schedule and manage flights (routes, timings)
- Handle passenger records
- Assign and manage crew members
- View and filter flights, passengers, and planes
- Role-based access for Admins and Users

# 🛍️ Shop Management
- Add and manage shop details (name, location, type)
- Manage shop inventory (products, prices, stock)
- Record transactions/sales
- Generate reports on sales and inventory
- Track low-stock and best-selling products

# ⚙️ Installation
You can install this app using the [bench ](https://github.com/frappe/bench)CLI:

<pre>cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app airplane_mode</pre>

# 🤝 Contributing
This app uses pre-commit for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

Go to the app folder:

<pre>
cd apps/management
pre-commit install</pre>



