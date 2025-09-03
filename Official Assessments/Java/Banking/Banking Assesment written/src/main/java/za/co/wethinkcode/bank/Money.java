package za.co.wethinkcode.bank;

import java.text.DecimalFormat;

public class Money implements Comparable<Money>
{
    public static final Money ZERO = new Money( 0 );
    public long amount;

    public Money(long amount){
        this.amount = amount;
    }

    public Money add(Money insantace){
        return new Money(amount + insantace.amount);
    }

    public Money subtract(Money insantace){
        return new Money(amount - insantace.amount);
    }

    public String formattedAsRands(){
        return new DecimalFormat("R0.00").format((double)amount/100);
    }


    @Override
    public int compareTo(Money instance){
        return Long.compare(amount, instance.amount);
    }

    @Override
    public boolean equals(Object instance){
        if(instance == this) return true;
        if(instance == null || instance.getClass() != getClass()) return false;

        Money other = (Money) instance;
        return amount == other.amount;
    }

    @Override
    public String toString(){
        return formattedAsRands();
    }


}
