import shapes.Circle;
import shapes.Rectangle;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class ShapeTest {
    @Test
    void testCircleAreaAndPerimeter() {
        Circle c = new Circle(2);
        assertEquals(Math.PI * 4, c.calculateArea(), 0.01);
        assertEquals(2 * Math.PI * 2, c.calculatePerimeter(), 0.01);
    }

    @Test
    void testRectangleAreaAndPerimeter() {
        Rectangle r = new Rectangle(4, 5);
        assertEquals(20, r.calculateArea(), 0.01);
        assertEquals(18, r.calculatePerimeter(), 0.01);
    }
}
