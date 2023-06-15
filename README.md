# JustASimpleInterviewGradingSystem 

This README provides an overview of the Interview System, its functionalities, and the process it follows for conducting interviews and evaluating the performance of interviewees. The system incorporates various events such as resume summary extraction, resume-related question generation, text-to-speech for question presentation, speech-to-text for recording interviewee answers, and evaluation of answers. The system also stores evaluation results as CSV records and calculates the final performance of the interview based on multiple factors.

## Functionality

The Interview System is designed to streamline the interview process by automating several tasks. The main functionalities of the system are as follows:

1. **Resume Summary Extraction:** The system extracts a summary of the interviewee's resume to gather relevant information for the interview process.

2. **Resume Related Question Generation:** Based on the extracted resume summary, the system generates interview questions that are relevant to the interviewee's background and experience.

3. **Text-to-Speech Question Presentation:** The generated questions are displayed to the user and read out using text-to-speech technology, allowing the interviewee to hear the questions.

4. **Speech-to-Text Answer Recording:** The interviewee answers the questions using their voice, and the system converts their speech into text using speech-to-text technology. The recording of the answer is restricted to a maximum of 2 minutes.

5. **Answer Evaluation:** The system evaluates each answer individually based on predefined criteria. If the grade for a question is below the average grade, a follow-up question is generated and evaluated.

6. **CSV Record Storage:** The evaluations for each question, including the primary questions and follow-up questions, are stored in a list of CSV records for future reference and analysis.

7. **Final Performance Evaluation:** The final performance of the interviewee is calculated based on multiple factors, including the summary of their resume, the job role they applied for, their experience, and their performance in the interview. All these factors are considered in the evaluation process.

## Getting Started

To use the Interview System, follow these steps:

1. **Installation:** Install the required dependencies and libraries mentioned in the system's documentation.

2. **Resume Summary Extraction:** Provide the interviewee's resume as input to extract a summary using the system's resume summary extraction module.

3. **Resume Related Question Generation:** The system will generate relevant interview questions based on the extracted resume summary.

4. **Question Presentation:** The generated questions will be displayed to the interviewee and read out using text-to-speech technology.

5. **Answer Recording:** The interviewee will answer the questions using their voice, and the system will convert their speech into text using speech-to-text technology. The recording is limited to a maximum of 2 minutes.

6. **Answer Evaluation:** The system will evaluate each answer individually based on predefined criteria, generating follow-up questions if necessary.

7. **CSV Record Storage:** The evaluations for each question, including the primary questions and follow-up questions, will be stored as CSV records for future reference and analysis.

8. **Final Performance Evaluation:** The final performance of the interviewee will be calculated based on the summary of their resume, the job role they applied for, their experience, and their performance in the interview.

## Contributions and Feedback

Contributions to the Interview System are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the system's GitHub repository. Your feedback will help make the system more efficient and user-friendly.

## License

The Interview System is open source and is licensed under the [GNU License](https://opensource.org/licenses/GNU_v2). Feel free to use, modify, and distribute the system in accordance with the license terms.

## Acknowledgements

The Interview System was developed with the help of various open-source libraries and

 technologies. We would like to express our gratitude to the developers and contributors of these projects for their valuable work.

If you have any further questions or need assistance with the Interview System, please refer to the system's documentation or contact our support team.

Thank you for using the Interview System!

