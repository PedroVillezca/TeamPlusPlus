program objects;

class Cat {
    attributes
        private char eyeColor;
    methods
        public func void meow() {
            print("Meow... \n");
        }

        public func void setEyeColor(char color) {
            eyeColor = color;
        }
        public func char getEyeColor() {
            return(eyeColor);
        }
};

vars
    Cat tom;

main() {
    vars
        char color = 'r';

    tom.meow();
    tom.setEyeColor(color);
    print(tom.getEyeColor());
}