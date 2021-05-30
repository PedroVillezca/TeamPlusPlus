program expressions;

main() {
    vars
        int w = 2, x = 13, y = -3, z = 32, expr1;
        float a = 3.21, b = 67.45, c = 22.5298, expr2;
        int i, j, k, expr3;
    
    expr1 = w + (-x - y) - +z;
    expr2 = ((b / a) * -c) / expr1;
    expr3 = not((a >= w) or (b < x) and c != z);

    print(expr1, "\n");
    print(expr2, "\n");
    print(expr3, "\n");
}