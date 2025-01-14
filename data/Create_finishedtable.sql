CREATE TABLE Product (
  /* 중고, 당근, 번장 3 개의 테이블을 하나로 합침 */
  
  /* 최종 테이블 생성 */
  id bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  site_name varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  article_url varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  title varchar(5000) COLLATE utf8mb4_unicode_ci NOT NULL,
  price bigint(20) COLLATE utf8mb4_unicode_ci,
  image varchar(255) COLLATE utf8mb4_unicode_ci,
  published_at datetime NOT NULL,
  crawled_at datetime NOT NULL,
  PRIMARY KEY (id)
)DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*중고, 당근, 번장의 데이터를 삽입함 */
insert into Product (site_name, article_url, title, price, image, published_at, crawled_at)
select site_name, article_url, title, price, image, published_at, crawled_at 
from bunjang;

insert into Product (site_name, article_url, title, price, image, published_at, crawled_at)
select site_name, article_url, title, price, image, published_at, crawled_at 
from danggn;

insert into Product (site_name, article_url, title, price, image, published_at, crawled_at)
select site_name, article_url, title, price, image, published_at_mod, crawled_at 
from junggo;