use testdb;

SELECT * FROM testdb.product;
/* product 테이블에서 특정 키워드를 제거하기 위함 */
delete from Product 
where title like '%삽니다%' or title like '%구해요%' or title like '%사요%' or title = '%구해봅니다%' or title like '%파실 분%';

select title from Product 
where  title = '%교환%' or title ='%구매%' or title = '%찾습니다%' or title = '%찾아요%' or title = '%매입%';

delete from Product  
where  title = '%교환%' or title ='%구매%' or title = '%찾습니다%' or title = '%찾아요%' or title = '%매입%';

select title from Product 
where title = '%구입%' or title = '%원해요%' or title = '%나눔%' or title = '%기부%';

delete from Product 
where title = '%구입%' or title = '%원해요%' or title = '%나눔%' or title = '%기부%';

/*가격, 이미지가 null인 행 삭제 */
delete from testdb.product where price is null;
delete from testdb.product where image is null;