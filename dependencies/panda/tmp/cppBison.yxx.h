/* A Bison parser, made by GNU Bison 2.7.  */

/* Bison interface for Yacc-like parsers in C
   
      Copyright (C) 1984, 1989-1990, 2000-2012 Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

#ifndef YY_CPPYY_BUILT_TMP_CPPBISON_YXX_H_INCLUDED
# define YY_CPPYY_BUILT_TMP_CPPBISON_YXX_H_INCLUDED
/* Enabling traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int cppyydebug;
#endif

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     REAL = 258,
     INTEGER = 259,
     CHAR_TOK = 260,
     SIMPLE_STRING = 261,
     SIMPLE_IDENTIFIER = 262,
     STRING_LITERAL = 263,
     CUSTOM_LITERAL = 264,
     IDENTIFIER = 265,
     TYPENAME_IDENTIFIER = 266,
     SCOPING = 267,
     TYPEDEFNAME = 268,
     ELLIPSIS = 269,
     OROR = 270,
     ANDAND = 271,
     EQCOMPARE = 272,
     NECOMPARE = 273,
     LECOMPARE = 274,
     GECOMPARE = 275,
     LSHIFT = 276,
     RSHIFT = 277,
     POINTSAT_STAR = 278,
     DOT_STAR = 279,
     UNARY = 280,
     UNARY_NOT = 281,
     UNARY_NEGATE = 282,
     UNARY_MINUS = 283,
     UNARY_PLUS = 284,
     UNARY_STAR = 285,
     UNARY_REF = 286,
     POINTSAT = 287,
     SCOPE = 288,
     PLUSPLUS = 289,
     MINUSMINUS = 290,
     TIMESEQUAL = 291,
     DIVIDEEQUAL = 292,
     MODEQUAL = 293,
     PLUSEQUAL = 294,
     MINUSEQUAL = 295,
     OREQUAL = 296,
     ANDEQUAL = 297,
     XOREQUAL = 298,
     LSHIFTEQUAL = 299,
     RSHIFTEQUAL = 300,
     KW_ALIGNAS = 301,
     KW_ALIGNOF = 302,
     KW_AUTO = 303,
     KW_BEGIN_PUBLISH = 304,
     KW_BLOCKING = 305,
     KW_BOOL = 306,
     KW_CATCH = 307,
     KW_CHAR = 308,
     KW_CHAR16_T = 309,
     KW_CHAR32_T = 310,
     KW_CLASS = 311,
     KW_CONST = 312,
     KW_CONSTEXPR = 313,
     KW_CONST_CAST = 314,
     KW_DECLTYPE = 315,
     KW_DEFAULT = 316,
     KW_DELETE = 317,
     KW_DOUBLE = 318,
     KW_DYNAMIC_CAST = 319,
     KW_ELSE = 320,
     KW_END_PUBLISH = 321,
     KW_ENUM = 322,
     KW_EXTENSION = 323,
     KW_EXTERN = 324,
     KW_EXPLICIT = 325,
     KW_PUBLISHED = 326,
     KW_FALSE = 327,
     KW_FINAL = 328,
     KW_FLOAT = 329,
     KW_FRIEND = 330,
     KW_FOR = 331,
     KW_GOTO = 332,
     KW_IF = 333,
     KW_INLINE = 334,
     KW_INT = 335,
     KW_LONG = 336,
     KW_MAKE_MAP_PROPERTY = 337,
     KW_MAKE_PROPERTY = 338,
     KW_MAKE_PROPERTY2 = 339,
     KW_MAKE_SEQ = 340,
     KW_MAKE_SEQ_PROPERTY = 341,
     KW_MUTABLE = 342,
     KW_NAMESPACE = 343,
     KW_NEW = 344,
     KW_NOEXCEPT = 345,
     KW_NULLPTR = 346,
     KW_OPERATOR = 347,
     KW_OVERRIDE = 348,
     KW_PRIVATE = 349,
     KW_PROTECTED = 350,
     KW_PUBLIC = 351,
     KW_REGISTER = 352,
     KW_REINTERPRET_CAST = 353,
     KW_RETURN = 354,
     KW_SHORT = 355,
     KW_SIGNED = 356,
     KW_SIZEOF = 357,
     KW_STATIC = 358,
     KW_STATIC_ASSERT = 359,
     KW_STATIC_CAST = 360,
     KW_STRUCT = 361,
     KW_TEMPLATE = 362,
     KW_THREAD_LOCAL = 363,
     KW_THROW = 364,
     KW_TRUE = 365,
     KW_TRY = 366,
     KW_TYPEDEF = 367,
     KW_TYPEID = 368,
     KW_TYPENAME = 369,
     KW_UNION = 370,
     KW_UNSIGNED = 371,
     KW_USING = 372,
     KW_VIRTUAL = 373,
     KW_VOID = 374,
     KW_VOLATILE = 375,
     KW_WCHAR_T = 376,
     KW_WHILE = 377,
     START_CPP = 378,
     START_CONST_EXPR = 379,
     START_TYPE = 380
   };
#endif
/* Tokens.  */
#define REAL 258
#define INTEGER 259
#define CHAR_TOK 260
#define SIMPLE_STRING 261
#define SIMPLE_IDENTIFIER 262
#define STRING_LITERAL 263
#define CUSTOM_LITERAL 264
#define IDENTIFIER 265
#define TYPENAME_IDENTIFIER 266
#define SCOPING 267
#define TYPEDEFNAME 268
#define ELLIPSIS 269
#define OROR 270
#define ANDAND 271
#define EQCOMPARE 272
#define NECOMPARE 273
#define LECOMPARE 274
#define GECOMPARE 275
#define LSHIFT 276
#define RSHIFT 277
#define POINTSAT_STAR 278
#define DOT_STAR 279
#define UNARY 280
#define UNARY_NOT 281
#define UNARY_NEGATE 282
#define UNARY_MINUS 283
#define UNARY_PLUS 284
#define UNARY_STAR 285
#define UNARY_REF 286
#define POINTSAT 287
#define SCOPE 288
#define PLUSPLUS 289
#define MINUSMINUS 290
#define TIMESEQUAL 291
#define DIVIDEEQUAL 292
#define MODEQUAL 293
#define PLUSEQUAL 294
#define MINUSEQUAL 295
#define OREQUAL 296
#define ANDEQUAL 297
#define XOREQUAL 298
#define LSHIFTEQUAL 299
#define RSHIFTEQUAL 300
#define KW_ALIGNAS 301
#define KW_ALIGNOF 302
#define KW_AUTO 303
#define KW_BEGIN_PUBLISH 304
#define KW_BLOCKING 305
#define KW_BOOL 306
#define KW_CATCH 307
#define KW_CHAR 308
#define KW_CHAR16_T 309
#define KW_CHAR32_T 310
#define KW_CLASS 311
#define KW_CONST 312
#define KW_CONSTEXPR 313
#define KW_CONST_CAST 314
#define KW_DECLTYPE 315
#define KW_DEFAULT 316
#define KW_DELETE 317
#define KW_DOUBLE 318
#define KW_DYNAMIC_CAST 319
#define KW_ELSE 320
#define KW_END_PUBLISH 321
#define KW_ENUM 322
#define KW_EXTENSION 323
#define KW_EXTERN 324
#define KW_EXPLICIT 325
#define KW_PUBLISHED 326
#define KW_FALSE 327
#define KW_FINAL 328
#define KW_FLOAT 329
#define KW_FRIEND 330
#define KW_FOR 331
#define KW_GOTO 332
#define KW_IF 333
#define KW_INLINE 334
#define KW_INT 335
#define KW_LONG 336
#define KW_MAKE_MAP_PROPERTY 337
#define KW_MAKE_PROPERTY 338
#define KW_MAKE_PROPERTY2 339
#define KW_MAKE_SEQ 340
#define KW_MAKE_SEQ_PROPERTY 341
#define KW_MUTABLE 342
#define KW_NAMESPACE 343
#define KW_NEW 344
#define KW_NOEXCEPT 345
#define KW_NULLPTR 346
#define KW_OPERATOR 347
#define KW_OVERRIDE 348
#define KW_PRIVATE 349
#define KW_PROTECTED 350
#define KW_PUBLIC 351
#define KW_REGISTER 352
#define KW_REINTERPRET_CAST 353
#define KW_RETURN 354
#define KW_SHORT 355
#define KW_SIGNED 356
#define KW_SIZEOF 357
#define KW_STATIC 358
#define KW_STATIC_ASSERT 359
#define KW_STATIC_CAST 360
#define KW_STRUCT 361
#define KW_TEMPLATE 362
#define KW_THREAD_LOCAL 363
#define KW_THROW 364
#define KW_TRUE 365
#define KW_TRY 366
#define KW_TYPEDEF 367
#define KW_TYPEID 368
#define KW_TYPENAME 369
#define KW_UNION 370
#define KW_UNSIGNED 371
#define KW_USING 372
#define KW_VIRTUAL 373
#define KW_VOID 374
#define KW_VOLATILE 375
#define KW_WCHAR_T 376
#define KW_WHILE 377
#define START_CPP 378
#define START_CONST_EXPR 379
#define START_TYPE 380



#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED

# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

#if ! defined YYLTYPE && ! defined YYLTYPE_IS_DECLARED
typedef struct YYLTYPE
{
  int first_line;
  int first_column;
  int last_line;
  int last_column;
} YYLTYPE;
# define yyltype YYLTYPE /* obsolescent; will be withdrawn */
# define YYLTYPE_IS_DECLARED 1
# define YYLTYPE_IS_TRIVIAL 1
#endif


#ifdef YYPARSE_PARAM
#if defined __STDC__ || defined __cplusplus
int cppyyparse (void *YYPARSE_PARAM);
#else
int cppyyparse ();
#endif
#else /* ! YYPARSE_PARAM */
#if defined __STDC__ || defined __cplusplus
int cppyyparse (void);
#else
int cppyyparse ();
#endif
#endif /* ! YYPARSE_PARAM */

#endif /* !YY_CPPYY_BUILT_TMP_CPPBISON_YXX_H_INCLUDED  */
