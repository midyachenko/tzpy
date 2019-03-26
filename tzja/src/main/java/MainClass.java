import org.openqa.selenium.WebDriver;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.firefox.FirefoxDriver;
import java.util.regex.Pattern;
import java.util.concurrent.TimeUnit;
import org.junit.*;



public class MainClass {

    public static void main(String[] args){
     System.setProperty("webdriver.gecko.driver", "C:\\GitRepo\\tzja\\drivers\\geckodriver.exe");

        WebDriver driver=new FirefoxDriver();
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS)
        driver.manage().window().maximize();

        //Кейс 1
        driver.get("https://www.google.com");
        System.out.println(driver.getTitle());
        driver.findElement(By.name("q")).click();
        driver.findElement(By.name("q")).clear();
        driver.findElement(By.name("q")).sendKeys("яндекс маркет");
        driver.findElement(By.name("q")).sendKeys(Keys.ENTER);
        driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='Веб-результат со ссылками на сайт'])[1]/following::h3[1]")).click();
        //Кейс 2
        driver.get("https://market.yandex.ru/");

        driver.findElement(By.id("header-search")).click();
        driver.findElement(By.id("header-search")).clear();
        driver.findElement(By.id("header-search")).sendKeys("пылесосы");
        driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='пылесосы'])[1]/following::button[1]")).click();
        driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='Показать всё'])[2]/following::span[1]")).click();
        driver.findElement(By.id("glf-priceto-var")).click();
        driver.findElement(By.id("glf-priceto-var")).clear();
        driver.findElement(By.id("glf-priceto-var")).sendKeys("6000");
        driver.findElement(By.linkText("Показать подходящие")).click();
        driver.findElement(By.id("header-search")).click();
        driver.findElement(By.id("header-search")).clear();
        driver.findElement(By.id("header-search")).sendKeys("пылесосы");
        driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='пылесосы'])[1]/following::button[1]")).click();
        driver.findElement(By.linkText("Все фильтры")).click();
        driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='Philips'])[1]/following::label[1]")).click();
        driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='Thomas'])[1]/following::label[1]")).click();
        driver.findElement(By.id("glf-priceto-var")).click();
        driver.findElement(By.id("glf-priceto-var")).clear();
        driver.findElement(By.id("glf-priceto-var")).sendKeys("6000");
        driver.findElement(By.linkText("Показать подходящие")).click();
        driver.quit();
    }


    }

}
