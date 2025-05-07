# Tutorial Avanzado de Dart: Conceptos Profesionales

Este tutorial cubre características avanzadas de Dart que te permitirán escribir código más profesional y eficiente. Asumimos que ya dominas los conceptos básicos del tutorial anterior.

## 1. Programación Asíncrona: Futures, async/await

Dart es single-threaded pero maneja operaciones asíncronas eficientemente.

### Futures básicos

```dart
Future<String> fetchUserData() {
  // Simulamos una operación que toma tiempo (como una API call)
  return Future.delayed(Duration(seconds: 2), () => 'Datos del usuario: Juan Pérez');
}

void main() {
  print('Iniciando...');
  fetchUserData().then((data) {
    print(data);
  });
  print('Esperando datos...');
}
```

### async/await

```dart
Future<void> mostrarDatosUsuario() async {
  try {
    print('Cargando...');
    var data = await fetchUserData(); // Espera sin bloquear el hilo
    print('Datos recibidos: $data');
  } catch (e) {
    print('Error: $e');
  }
}

void main() async {
  await mostrarDatosUsuario();
  print('Proceso completado');
}
```

**Ejercicio Avanzado 1**: Crea una función que:

1. Simule la descarga de 3 archivos (cada uno toma entre 1-3 segundos)
2. Espere a que todos se completen usando `Future.wait`
3. Procese los resultados juntos

## 2. Streams y Reactive Programming

Los Streams representan flujos de datos asíncronos.

```dart
import 'dart:async';

Stream<int> contarHastaDiez() async* {
  for (int i = 1; i <= 10; i++) {
    await Future.delayed(Duration(seconds: 1));
    yield i; // Emite un valor al stream
  }
}

void main() {
  final stream = contarHastaDiez();

  final subscription = stream.listen(
    (data) => print('Dato recibido: $data'),
    onError: (err) => print('Error: $err'),
    onDone: () => print('Stream completado'),
    cancelOnError: false
  );

  // Para cancelar: subscription.cancel();
}
```

**Ejercicio Avanzado 2**: Crea un Stream que emita:

1. Temperaturas aleatorias cada segundo
2. Filtre temperaturas mayores a 25°C
3. Detenga el stream después de 10 emisiones

## 3. Generics (Tipos Genéricos)

```dart
class Caja<T> {
  final T contenido;

  Caja(this.contenido);

  T abrir() => contenido;
}

void main() {
  var cajaString = Caja<String>('Sorpresa!');
  var cajaInt = Caja<int>(42);

  print(cajaString.abrir());
  print(cajaInt.abrir());
}
```

## 4. Extension Methods

Agrega funcionalidad a clases existentes.

```dart
extension StringExtension on String {
  String get capitalize =>
      this.length > 0 ? this[0].toUpperCase() + this.substring(1) : this;

  String get reverse => this.split('').reversed.join();
}

extension NumberParsing on String {
  int toIntOrZero() => int.tryParse(this) ?? 0;
}

void main() {
  print('dart'.capitalize); // Dart
  print('hello'.reverse); // olleh
  print('123'.toIntOrZero()); // 123
  print('abc'.toIntOrZero()); // 0
}
```

**Ejercicio Avanzado 3**: Crea extensiones para:

1. List: método `mixto` que devuelva la lista mezclada
2. DateTime: método `formatear` que devuelva "dd-MM-yyyy"

## 5. Null Safety Avanzado

Dart tiene null safety sólido. Veamos patrones avanzados.

```dart
class Usuario {
  final String nombre;
  final int? edad;

  Usuario({required this.nombre, this.age});

  void mostrarEdad() {
    if (edad case final edad? when edad > 0) {
      print('Edad: $edad');
    } else {
      print('Edad no disponible');
    }
  }
}

void main() {
  var user = Usuario(nombre: 'Ana', edad: null);
  user.mostrarEdad();

  // Pattern matching con switch
  var valor = 42;
  var descripcion = switch (valor) {
    > 50 => 'Grande',
    < 20 => 'Pequeño',
    _ => 'Mediano',
  };
  print(descripcion);
}
```

## 6. Concurrencia con Isolates

Dart usa isolates para concurrencia real (no threads).

```dart
import 'dart:isolate';

Future<void> calcularEnParalelo() async {
  final receivePort = ReceivePort();

  await Isolate.spawn(_calculoPesado, receivePort.sendPort);

  final resultado = await receivePort.first;
  print('Resultado: $resultado');
}

void _calculoPesado(SendPort sendPort) {
  // Simulamos un cálculo intensivo
  var total = 0;
  for (var i = 0; i < 1000000000; i++) {
    total += i;
  }
  sendPort.send(total);
}

void main() async {
  print('Iniciando cálculo en paralelo...');
  await calcularEnParalelo();
  print('Cálculo completado');
}
```

**Ejercicio Avanzado 4**: Crea un programa que:

1. Use 3 isolates para calcular factoriales de 20, 25 y 30
2. Combine los resultados cuando todos terminen

## 7. Metaprogramming con Reflection (mirrors)

```dart
import 'dart:mirrors';

class Producto {
  final String id;
  final String nombre;
  final double precio;

  Producto(this.id, this.nombre, this.precio);

  @override
  String toString() => 'Producto $id: $nombre (\$$precio)';
}

void mostrarPropiedades(Object objeto) {
  final instanceMirror = reflect(objeto);
  final classMirror = instanceMirror.type;

  print('Propiedades de ${classMirror.simpleName}:');

  for (var declaration in classMirror.declarations.values) {
    if (declaration is VariableMirror) {
      final name = MirrorSystem.getName(declaration.simpleName);
      final value = instanceMirror.getField(declaration.simpleName).reflectee;
      print(' - $name: $value (${declaration.type.simpleName})');
    }
  }
}

void main() {
  final producto = Producto('123', 'Laptop', 999.99);
  mostrarPropiedades(producto);
}
```

## 8. FFI (Foreign Function Interface)

Interactúa con código nativo (C/C++).

```dart
import 'dart:ffi';
import 'package:ffi/ffi.dart';

// Ejemplo con una librería C
final nativeLib = DynamicLibrary.open('lib/mi_libreria.so');

// Definición de la función C
typedef SumaFunc = Int32 Function(Int32, Int32);
typedef Suma = int Function(int, int);

void main() {
  final suma = nativeLib.lookupFunction<SumaFunc, Suma>('suma');

  final resultado = suma(5, 3);
  print('Resultado de suma desde C: $resultado');
}
```

**Ejercicio Avanzado 5**: (Requiere configuración adicional)

1. Crea una función en C que calcule el n-ésimo número de Fibonacci
2. Compílala como librería compartida
3. Llámala desde Dart usando FFI

## 9. Patrones de Diseño en Dart

### Singleton

```dart
class Database {
  static final Database _instance = Database._internal();

  factory Database() => _instance;

  Database._internal() {
    print('Conexión a DB inicializada');
  }

  void query(String sql) => print('Ejecutando: $sql');
}

void main() {
  var db1 = Database();
  var db2 = Database();

  print(identical(db1, db2)); // true, misma instancia

  db1.query('SELECT * FROM users');
}
```

### Factory Method

```dart
abstract class Logger {
  void log(String message);

  factory Logger(String type) {
    switch (type) {
      case 'file':
        return FileLogger();
      case 'console':
      default:
        return ConsoleLogger();
    }
  }
}

class ConsoleLogger implements Logger {
  @override
  void log(String message) => print('CONSOLE: $message');
}

class FileLogger implements Logger {
  @override
  void log(String message) => print('FILE: $message');
}

void main() {
  var logger = Logger('file');
  logger.log('Mensaje de error');
}
```

## 10. Testing Avanzado

```dart
// mi_biblioteca.dart
int suma(int a, int b) => a + b;
Stream<int> contador(int max) async* {
  for (var i = 1; i <= max; i++) {
    await Future.delayed(Duration(milliseconds: 100));
    yield i;
  }
}

// test_mi_biblioteca.dart
import 'package:test/test.dart';
import 'mi_biblioteca.dart';

void main() {
  group('Pruebas de suma', () {
    test('Suma positiva', () {
      expect(suma(2, 3), equals(5));
    });

    test('Suma con cero', () {
      expect(suma(0, 5), equals(5));
    });
  });

  group('Pruebas de contador', () {
    test('Emite valores correctos', () async {
      final stream = contador(3);
      await expectLater(stream, emitsInOrder([1, 2, 3]));
    });

    test('Completa después de emitir', () async {
      final stream = contador(1);
      await expectLater(stream, emits(1));
      await expectLater(stream, emitsDone);
    });
  });
}
```

**Ejercicio Final Avanzado**:
Crea un paquete Dart que incluya:

1. Una clase con métodos complejos (ej: procesamiento de datos)
2. Tests unitarios con casos edge
3. Documentación usando dartdoc
4. Un ejemplo de uso con async/await
5. Un isolate para operaciones pesadas

Ejecuta los tests con: `dart test`

---

Este tutorial avanzado cubre características profesionales de Dart. Para profundizar:

- Explora paquetes populares como `riverpod` para state management
- Aprende sobre code generation con `build_runner`
- Investiga interoperabilidad con Flutter y web
- Estudia arquitecturas limpias y patrones de diseño adicionales

¡Lleva tus habilidades de Dart al siguiente nivel! 🚀
