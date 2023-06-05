package com.ssafy.factorymethod;
public class AnotherConcreteCreator extends Creator {
    
    protected Product factoryMethod() {
        return new AnotherConcreteProduct();
    }
}