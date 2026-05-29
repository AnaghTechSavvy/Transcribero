# Transcribero 🧬

An interactive command-line utility built in Python using the **Biopython** library. This tool allows users to securely authenticate and batch-process multiple DNA sequences simultaneously, transcribing them into their corresponding mRNA strands.

---

## 🚀 Features

* **Secure Entry Gate:** Simple integer password validation before granting access to data processing.
* **Batch Collection:** Utilizes stateful loops to dynamically gather multiple sequences from user input before execution.
* **Biopython Processing Engine:** Leverages standard computational biology objects (`Seq`) for flawless transcription.
* **User-Sanitized Input:** Automatically handles case insensitivity (converts lowercase inputs to uppercase) and strips accidental whitespaces.

---

## 🛠️ How It Works

1. The program prompts the user to create and confirm a temporary session password.
2. Upon successful authentication, the user enters DNA sequences one by one.
3. Typing `DONE` breaks the collection loop and triggers the batch processing engine.
4. The tool loops through the collected data structure, executes `.transcribe()`, and outputs the results before pausing for user review.

---

## 💻 How to Run It Locally

To run this tool on your own machine, follow these simple steps:

1. **Clone the repository or download the script:**
   ```bash
   git clone [https://github.com/AnaghTechSavvy/Transcribero.git](https://github.com/AnaghTechSavvy/Transcribero.git)
