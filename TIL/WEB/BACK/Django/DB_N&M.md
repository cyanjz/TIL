# 개요
Database에서 중개 테이블을 생성하여 다대다 관계를 형성하는 것을 django에서 어떻게 구현하는지 기술.

개념적으로는 A, B 테이블에서 중개 테이블을 역참조 하는 것.

그러나 `ManyToManyField`를 사용하면 해당 필드가 참조하는 모델이 해당 필드를 정의한 모델을 역참조한다.

**핵심**
```python
# model_B에 정의해서 model_A와의 관계를 정의하는 필드.
{relation}_{model_A}s = models.ManyToManyField({model_A},
                                                related_name='{relation}_{model_B}s',
                                                through='{relation_table}',)
# 참조하는 모델이 자기 자신이라면 'self'를 첫번째 인자로 준다.


# 중개 테이블에 정보를 추가해서 through 인자를 사용하여 ManyToManyField를 정의한 경우
# throuh_defaults를 사용해서 add를 호출해야한다.
A_instance.relation_Bs.add(B_instance, through_defaults={'field' : 'value', ...})
# 삭제는 remove.
A_instance.relation_Bs.remove(B_instance)
```

# 모델 필드 선언
## 중개 모델을 직접 선언 (비권장)
```python
class Doctor(models.Model):
    name = models.TextField()

class Patient(models.Model):
    name = models.TextField()

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.FOreignKey(Patient, on_delete=models.CASCADE)
```

- 관련 문법
```python
# reservation table 역참조
doctor1.reservation_set.all()
patient1.reservation_set.all()
# 새로운 M:N 관계 만들기
Reservation.objects.create(doctor=doctor1, patient=patient2)
```

## ManyToManyField (권장)
`ManyToManyField(to, **options)`

Many to Many field를 선언할 때는 관계를 맺는 테이블 둘 중 아무거나 하나에 필드를 다음과 같이 선언한다.

필드 명과 `related_name`인자는 필수는 아니지만, 관계를 맺는 경우가 많아짐에 따라서 참조와 역참조의 명칭을 관리하기 위해서 작성. (작성하지 않을 경우에 충돌이 발생할 수 있다.)
```python
# model_B에 정의해서 model_A와의 관계를 정의하는 필드.
{relation}_{model_A}s = models.ManyToManyField({model_A}, related_name='{relation}_{model_B}s')
```

### 예제

```python
class Doctor(models.Model):
    name = models.TextField()

class Patient(models.Model):
    name = models.TextField()
    reservation_doctors = models.ManyToManyField(Doctor, related_name='reservation_patients')
```

### 관계 형성
```python
# doctor1, patient1에 add를 통해 관계 형성
doctor1.reservation_patients.add(patient1)
patient1.reservation_doctors.add(doctor1)

# doctor1, patient1에 remove를 통해 관계를 삭제
doctor1.reservation_doctors.remove(patient1)
patient1.reservation_doctors.remove(doctor1)
```

### 대표 인자
#### related_name
역참조의 method 이름을 지정.
#### through
중개 테이블에 추가 정보를 넣고 싶을 때 지정하는 인자.

중개 테이블을 별도로 정의하고, through 인자에 string 형태로 넣어준다.

```python
class Patient(models.Model):
    name = models.TextField()
    reservation_doctors = models.ManyToManyField(Doctor,
                                                related_name='reservation_patients',
                                                through='Reservation',)

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    decease = models.TextField()
```

중개 테이블을 형성한 경우에 M:N 관계를 만들 경우에는 추가 인자를 줘서 만들어야 한다.
```python
patient1 = Patient.objects.create(name='asdf')
doctor1 = Doctor.objects.create(name='qwer')

patient1.reservation_doctors.add(doctor1, through_defaults={'decease':'headache'})
doctor1.reservation_patients.add(patient1, through_defaults={'decease':'headache'})

patient1.reservation_doctors.remove(patient1)
```

#### symmetrical
재귀적 모델 관계에서 pk : 1 -> 2의 관계가 존재할 경우에 2 -> 1의 관계도 만들어준다.