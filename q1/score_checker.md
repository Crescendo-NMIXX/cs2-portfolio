# PSHS Student Score Checker

## Part 1 - Analyze the Logic

### Input
The program needs the student's score.

### Minimum Valid Score
The minimum valid score is **0**.

### Maximum Valid Score
The maximum valid score is **100**.

### Possible Outputs
The program can produce the following outputs:

- Invalid Score.
- Outstanding
- Very Satisfactory
- Satisfactory
- Needs Improvement

### Selection Pattern - Boundary Condition
The boundary condition is the validation that checks if the score is outside the valid range of 0 to 100.

Condition:
`score < 0 OR score > 100`

### Selection Pattern - Multiple Decision Paths
The grade classification uses multiple decision paths:

- 90–100 = Outstanding
- 80–89 = Very Satisfactory
- 75–79 = Satisfactory
- Below 75 = Needs Improvement


## Part 2 - Create the Flowchart



## Part 3 - Pseudocode

START

INPUT student_score

IF student_score < 0 OR student_score > 100 THEN
    DISPLAY "Invalid Score."
ELSE IF student_score >= 90 THEN
    DISPLAY "Outstanding"
ELSE IF student_score >= 80 THEN
    DISPLAY "Very Satisfactory"
ELSE IF student_score >= 75 THEN
    DISPLAY "Satisfactory"
ELSE
    DISPLAY "Needs Improvement"

END


## Part 5 - Test the Program

| Test | Input | Purpose                     |  Expected Output  |    Actual Output  | Result |
|------|-------|-----------------------------|-------------------|-------------------|--------|
| 1    | -1    | Below minimum               | Invalid Score.    | Invalid Score.    |  PASS  |
| 2    | 0     | Minimum boundary            | Needs Improvement | Needs Improvement |  PASS  |
| 3    | 74    | Below Satisfactory boundary | Needs Improvement | Needs Improvement |  PASS  |
| 4    | 75    | Satisfactory boundary       | Satisfactory      | Satisfactory      |  PASS  |
| 5    | 80    | Very Satisfactory boundary  | Very Satisfactory | Very Satisfactory |  PASS  |
| 6    | 90    | Outstanding boundary        | Outstanding       | Outstanding       |  PASS  |
| 7    | 100   | Maximum boundary            | Outstanding       | Outstanding       |  PASS  |
| 8    | 101   | Above maximum               | Invalid Score.    | Invalid Score.    |  PASS  |


## Testing Reflection

### 1. Why is it important to test the values 0 and 100?

It is important to test 0 and 100 because they are the minimum and maximum valid scores. This makes sure the program accepts the valid boundaries correctly.

### 2. Why did you also test -1 and 101?

I tested -1 and 101 to make sure the program rejects scores that are outside the valid range.

### 3. Which test helped you understand boundary conditions the most?

Testing 75, 80, and 90 helped me understand boundary conditions because these scores are where the classifications change.

### 4. Did any of your tests initially fail? If yes, what did you change in your program?

No, none of the tests initially failed. The program correctly handled the validation and classification conditions.


# Reflection

### 1. How did selection structures make the program more useful?

Selection structures allowed the program to make decisions based on the student's score and automatically give the correct classification.

### 2. How did proper comments and readable formatting improve your program?

Proper comments explain the important parts of the code, while readable formatting makes the program easier to understand and maintain.

### 3. Why is it useful to plan the program using a flowchart and pseudocode before writing the code?

A flowchart and pseudocode help organize the program's logic before coding. They also make it easier to find mistakes and understand the different decisions the program needs to make.
