package codes._2025._10;

import java.util.Scanner;

// 抽象クラス:全ての演算の共通の型
abstract class Operation {
    double a, b;

    Operation(double a, double b) {
        this.a = a;
        this.b = b;
    }

    abstract double calculate(); // サブクラスで実装
}

public class OopCalculator {

}
