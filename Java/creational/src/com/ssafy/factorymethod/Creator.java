package com.ssafy.factorymethod;
public abstract class Creator {
    protected abstract Product factoryMethod();
    
    public Product createOperation(){
        return factoryMethod();
    }
}
        