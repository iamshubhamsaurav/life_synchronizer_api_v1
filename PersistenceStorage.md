**Title: A JSON-Based Object-Oriented Configuration Storage System for JavaScript Desktop Applications**

---

### Abstract

Modern JavaScript desktop applications, particularly those built using frameworks like Electron, require efficient mechanisms to persist application and user configuration data. This paper presents a lightweight, persistent, and object-oriented key-value storage system using JSON files, designed to mimic the behavior of Android's SharedPreferences. The system is implemented entirely in JavaScript, offering a simple yet powerful API to read, write, and manage configuration values. Through object-oriented principles, the design promotes modularity, ease of maintenance, and extensibility. By avoiding the overhead of a relational database, the system remains focused, efficient, and resource-conscious—doing one thing and doing it exceptionally well. Instead of one shared file, the design stores different types of configuration data in multiple JSON files within a designated directory, ensuring clean separation and modular access.

---

### 1. Introduction

As desktop applications increasingly adopt JavaScript for cross-platform development, the need for reliable local storage systems has grown. While databases and external storage libraries exist, they are often overkill for storing small, structured configuration data such as user preferences, UI state, and lightweight metadata. Android developers benefit from SharedPreferences, a straightforward interface to store key-value pairs. A similar tool is lacking in the JavaScript desktop ecosystem.

This paper introduces a directory-based configuration storage system using multiple JSON files, adhering to object-oriented programming (OOP) paradigms. The system offers persistent, atomic storage of key-value pairs, making it suitable for managing app settings and user preferences with minimal setup. Each logical category of configuration data (e.g., `ui.json`, `network.json`, `auth.json`) resides in its own file, aiding organization and minimizing file size.

---

### 2. Background and Related Work

Persistent storage in JavaScript applications typically falls into three categories: in-memory stores, browser localStorage (for web apps), and embedded databases like SQLite or NeDB. Each comes with trade-offs in complexity, performance, and overhead. JSON files offer a middle ground: readable, native to JavaScript, and easy to version or transfer.

Using a traditional relational database (RDBMS) for storing application configurations introduces unnecessary baggage. RDBMS systems like SQLite or PostgreSQL bring with them layers of schema design, query syntax, data type constraints, transaction management, and dependency handling. These complexities are not only superfluous but also resource-intensive when the primary goal is to store a few simple user preferences or application settings.

In contrast, a JSON-based system focuses on doing one task—storing and retrieving key-value configurations—extremely well. It avoids needless abstractions and keeps the application architecture clean, readable, and maintainable. Additionally, JSON storage is particularly appealing in environments like Electron where JSON manipulation and filesystem access are native and straightforward.

SharedPreferences on Android inspired this system due to its simplicity and reliability. Additionally, insights from distributed key-value storage design (Nikasakana, 2021) inform certain safety mechanisms like atomic writes. However, this system focuses exclusively on local JSON storage, emphasizing clarity and simplicity.

---

### 3. Design Goals

* **JSON-Based Persistence**: Store configuration data in multiple JSON files organized within a directory.
* **OOP Architecture**: Encapsulate functionality in class-based modules for extensibility and clarity.
* **Simplicity and Usability**: Provide a minimal API: `get`, `set`, with intuitive instantiation.
* **Atomic and Durable Writes**: Prevent data corruption during updates using temporary file strategies.
* **Separation of Concerns**: Use different files for different configuration domains.
* **Developer Transparency**: Use a human-readable format suitable for debugging or manual editing.
* **Lightweight Footprint**: Avoid traditional database engines and reduce system complexity.

---

### 4. System Architecture

The core of the system is an object that represents a configuration store. Each instance corresponds to a unique JSON file used to persist key-value data. These objects abstract away the complexities of file I/O, caching, and atomic writes, exposing a minimal and intuitive interface.

#### Example Usage

```javascript
configStore = PersistenceStorage('configStore');

configStore.set('theme', 'dark');
const value = configStore.get('theme');
```

This illustrates the essence of the API. The `PersistenceStorage` constructor creates or loads a JSON file named `configStore.json`. The `set()` method updates a key-value pair, and `get()` retrieves it.

---

### 5. Use Cases

* Storing UI preferences like theme, language, layout
* Managing lightweight credentials or tokens
* Persisting application behavior settings
* Modular plugin or component configuration

Because each data domain is stored in a separate JSON file, developers gain clarity, maintainability, and flexibility. The design easily accommodates growing project complexity without increasing runtime overhead or architectural burden.

---

### 6. Security and Reliability

* **File Permissions**: Leverages OS-level file security.
* **Atomic Writes**: Writes occur to temporary files that are atomically renamed.
* **Isolation**: A single corrupted file does not affect others.
* **No Dependency Overhead**: Avoids bulky database engines and schema enforcement.

The design adheres to a UNIX-like philosophy: do one thing and do it well. It avoids monolithic architecture in favor of simple, composable components.

---

### 7. Future Enhancements

* **Encryption**: Secure sensitive values within files
* **Validation**: Optional schema checks before writing
* **Asynchronous Operations**: Promise-based async I/O support
* **Live Reloading**: Watch for file changes
* **Profile Support**: Named sets of configurations

---

### 8. Conclusion

This JSON-based, object-oriented configuration storage system provides an elegant solution for managing settings in JavaScript desktop applications. By simplifying the storage model to key-value pairs persisted in discrete JSON files, the system eliminates the need for bloated relational databases and third-party libraries. The result is a reliable, modular, and developer-friendly approach to configuration management. With minimal dependencies and maximum clarity, it performs one task—configuration storage—with focused excellence.

---

### References
