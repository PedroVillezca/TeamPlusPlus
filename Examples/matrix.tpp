program matrix;

vars
    float m1[3,3], m2[3,3], m3[3,3];

func void multiply() {
    vars
        int i, j, k;
        
    from i=0 to 2 {
        from j=0 to 2 {
            from k=0 to 2 {
                m3[i,j] = m1[i, k] * m2[k, j] + m3[i, j];
            }
        }
    }
}

main() {
    vars
        int i, j;
    
    from i=0 to 2 {
        from j=0 to 2 {
            read(m1[i, j]);
        }
    }

    from i=0 to 2 {
        from j=0 to 2 {
            print(m1[i,j], "\t");
        }
        print("\n");
    }

    from i=0 to 2 {
        from j=0 to 2 {
            read(m2[i, j]);
        }
    }

    from i=0 to 2 {
        from j=0 to 2 {
            print(m2[i,j], "\t");
        }
        print("\n");
    }

    from i=0 to 2 {
        from j=0 to 2 {
            m3[i, j] = 0.0;
        }
    }

    multiply();

    from i=0 to 2 {
        from j=0 to 2 {
            print(m3[i,j], "\t");
        }
        print("\n");
    }
}