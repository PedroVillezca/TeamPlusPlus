program oop;

class Person {
    attributes
        public int age;
        private float weight, height;

    methods
        public func int getAge() {
            return(age);
        }

        public func float getWeight() {
            return(weight);
        }

        public func void setWeight(float w) {
            weight = w;
        }

        public func float getHeight() {
            return(height);
        }

        public func void setHeight(float h) {
            height = h;
        }
        
        private func float calculateBMI() {
            vars
                float BMI;

            BMI = weight / (height * height);
            return(BMI);
        }

        public func float getBMI() {
            return(calculateBMI());
        }
};

class Student inherits Person {
    attributes
        private float grades[3];
    methods
        public func void setGrades() {
            vars
                int i;
            print("Ingresa calificaciones: ");
            from i=0 to 2 {
                read(grades[i]);
            }
        }

        private func float calculateAverage(){
            vars
                int i=0;
                float sum = 0.0;

                while (i < 3) {
                    sum = sum + grades[i];
                    i = i+1;
                }
                return(sum / 3);
        }

        public func char getGrade() {
            vars
                float avg = calculateAverage();
            
            if (avg >= 90) {
                return('A');
            } elif (avg >= 80) {
                return('B');
            } elif  (avg >= 70) {
                return('C');
            }
            return('D');
        }
};

vars
    Person enrique;
    Student beto;

main() {
    vars        
        int age;
        float weight, height;
    
    print("Ingresa edad: ");
    read(age);
    enrique.age = age;

    print("Ingresa peso: ");
    read(weight);
    enrique.setWeight(weight);

    print("Ingresa altura: ");
    read(height);
    enrique.setHeight(height);

    print("BMI is ", enrique.getBMI(), " at age ", enrique.age, "\n");

    print("Ingresa edad: ");
    read(age);
    beto.age = age;

    print("Ingresa peso: ");
    read(weight);
    beto.setWeight(weight);

    print("Ingresa altura: ");
    read(height);
    beto.setHeight(height);

    beto.setGrades();
    
    print("BMI is ", beto.getBMI(), " at age ", beto.age, "\n");
    print("Grade letter is: ", beto.getGrade(), "\n");
}