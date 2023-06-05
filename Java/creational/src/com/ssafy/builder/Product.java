package com.ssafy.builder;

public class Product {
	
    //required parameters
    private String HDD;
    private String RAM;
	
    //optional parameters
    private boolean isGraphicsCardEnabled;
    private boolean isBluetoothEnabled;
	
 
    public String getHDD() {
        return HDD;
    }
 
    public String getRAM() {
        return RAM;
    }
 
    public boolean isGraphicsCardEnabled() {
        return isGraphicsCardEnabled;
    }
 
    public boolean isBluetoothEnabled() {
        return isBluetoothEnabled;
    }
	
    private Product(ProductBuilder builder) {
        this.HDD=builder.HDD;
        this.RAM=builder.RAM;
        this.isGraphicsCardEnabled=builder.isGraphicsCardEnabled;
        this.isBluetoothEnabled=builder.isBluetoothEnabled;
    }
	
    //Builder Class
    public static class ProductBuilder{
 
        // required parameters
        private String HDD;
        private String RAM;
 
        // optional parameters
        private boolean isGraphicsCardEnabled;
        private boolean isBluetoothEnabled;
		
        public ProductBuilder(String hdd, String ram){
            this.HDD=hdd;
            this.RAM=ram;
        }
 
        public ProductBuilder setGraphicsCardEnabled(boolean isGraphicsCardEnabled) {
            this.isGraphicsCardEnabled = isGraphicsCardEnabled;
            return this;
        }
 
        public ProductBuilder setBluetoothEnabled(boolean isBluetoothEnabled) {
            this.isBluetoothEnabled = isBluetoothEnabled;
            return this;
        }
		
        public Product build(){
            return new Product(this);
        }
 
    }

	@Override
	public String toString() {
		return "Product [HDD=" + HDD + ", RAM=" + RAM + ", isGraphicsCardEnabled=" + isGraphicsCardEnabled
				+ ", isBluetoothEnabled=" + isBluetoothEnabled + "]";
	}
 
    
}
