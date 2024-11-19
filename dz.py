class Partner {
  final String gender; // Пол ("мужчина", "женщина")
  final int age; // Возраст
  final String hairColor; // Цвет волос
  final double height; // Рост (в см)
  final double weight; // Вес (в кг)
  final String city; // Город проживания
  final bool hasChildren; // Наличие детей
  final String education; // Уровень образования
  final bool hasTattoos; // Наличие татуировок
  final bool hasPiercings; // Наличие пирсинга
  final List<String> interests; // Список интересов

  Partner({
    required this.gender,
    required this.age,
    required this.hairColor,
    required this.height,
    required this.weight,
    required this.city,
    required this.hasChildren,
    required this.education,
    required this.hasTattoos,
    required this.hasPiercings,
    required this.interests,
  });
}

bool isPotentialPartner(
    Partner partner, String userCity, List<String> userInterests) {
  // Проверка базовых условий
  bool baseCriteria = partner.gender == "женщина" &&
      partner.age >= 20 &&
      partner.age <= 25 &&
      partner.height > 175 &&
      partner.weight < 60 &&
      partner.city == userCity &&
      !partner.hasChildren &&
      partner.education == "высшее" &&
      !partner.hasTattoos &&
      !partner.hasPiercings;

  // Проверка общих интересов
  int commonInterestsCount = partner.interests
      .where((interest) => userInterests.contains(interest))
      .length;

  return baseCriteria && commonInterestsCount > 5;
}

void main() {
  // Данные пользователя
  String userCity = "Москва";
  List<String> userInterests = [
    "спорт",
    "музыка",
    "чтение",
    "путешествия",
    "кино",
    "танцы"
  ];

  // Потенциальные партнеры
  List<Partner> partners = [
    Partner(
      gender: "женщина",
      age: 23,
      hairColor: "русый",
      height: 178,
      weight: 55,
      city: "Москва",
      hasChildren: false,
      education: "высшее",
      hasTattoos: false,
      hasPiercings: false,
      interests: ["спорт", "музыка", "чтение", "рисование", "танцы", "кино"],
    ),
    Partner(
      gender: "женщина",
      age: 26,
      hairColor: "блондин",
      height: 170,
      weight: 58,
      city: "Москва",
      hasChildren: false,
      education: "высшее",
      hasTattoos: false,
      hasPiercings: false,
      interests: ["спорт", "музыка", "чтение"],
    ),
    Partner(
      gender: "женщина",
      age: 22,
      hairColor: "шатен",
      height: 180,
      weight: 58,
      city: "Москва",
      hasChildren: false,
      education: "высшее",
      hasTattoos: false,
      hasPiercings: false,
      interests: ["спорт", "музыка", "чтение", "путешествия", "танцы", "кино"],
    ),
  ];

  // Фильтрация и вывод результата
  for (var partner in partners) {
    if (isPotentialPartner(partner, userCity, userInterests)) {
      print("Подходит: ${partner.interests}");
    } else {
      print("Не подходит");
    }
  }
}
