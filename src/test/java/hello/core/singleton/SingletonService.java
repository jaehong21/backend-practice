package hello.core.singleton;

public class SingletonService {

    private static final SingletonService instance = new SingletonService();

    public static SingletonService getInstance() {
        return instance;
    }

    private SingletonService() {
    }
    // private 생성자로 생성을 막아버림
    // 굉장히 중요함, 외부에서 2번째 객체가 생성되지 않도록

    public void logic() {
        System.out.println("싱글톤 객체 로직 호출");
    }

}
