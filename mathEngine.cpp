#include <cstdlib>
#include <ctime>
#include <string>

extern "C" {
    int a = 0, b = 0;

    // Generate a new question
    const char* get_question(){
        std::srand(std::time(nullptr));
        a = std::rand() % 12 + 1;
        b = std::rand() % 12 + 1;
        static std::string question;
        question = "What is " + std::to_string(a) + " x " 
                    + std::to_string(b) + "?";
        return question.c_str();
    }

    // Check the user's answer
    int check_answer(int user_input){
        return (user_input == a * b);
    }
}