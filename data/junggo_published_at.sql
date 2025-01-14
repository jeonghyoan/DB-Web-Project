
/*중고나라 published_at 데이터 포맷 처리 -> '%Y-%m-%d %H:%i:%s'포맷으로 변환하기 */ 

alter table articles3 add published_at_mod varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL after published_at;
update articles3 set published_at_mod=crawled_at;
update articles3 set published_at= str_to_date(published_at, '%H:%i') where published_at like'%:%';
update articles3 set published_at_mod=substring_index(published_at_mod," ",1);
UPDATE articles3 SET published_at_mod = STR_TO_DATE(published_at_mod, '%Y-%m-%d %H:%i:%s');
update articles3 set published_at_mod=addtime(published_at_mod,published_at) where published_at like'%:%';

/*중고나라 모든 상품 이미지 중고나라 공식 이미지로 변경 */
update articles3
set image = 'https://www.joongna.com/_nuxt/img/ci_web.11a1eb7.png';
